#!/usr/bin/env python
#
# Specification 2 prototype.
# By Jacob Joaquin
# jacobjoaquin@gmail.com

import os
import re
import string
import sys

def do_alwayson(csdx):
    '''Append a list of alwayson statements, and return a csdx with
    the statements removed.'''
    
    c = []
    alwayson = []
    
    p = re.compile('alwayson')
    
    for line in csdx.splitlines():
        m = p.match(line)
        
        if m:
            alwayson.append(line)
        else:
            c.append(line)
 
    return prepend_score('\n'.join(c), gen_alwayson_events(alwayson))

def do_definstrs(csdx, definstr_dict):
    m = re.findall('(definstr\s+.*?enddef)', csdx, re.DOTALL)

    if m:
        for d in m:
            definstr_dict.add(d)
            csdx = csdx.replace(d, '', 1)
        
    return csdx
    
def do_imports(csdx, definstr_dict):
    '''Adds definstr to dictionary and returns the csdx with the import
    statements removed.'''
    
    c = []
    p = re.compile('import ')
    
    for line in csdx.splitlines():
        m = p.match(line)
        
        if m:
            definstr_dict.add(import_definstr(line))
        else:
            c.append(line)
            
    return '\n'.join(c)

def do_newinstrs(csdx, definstr_dict):
    c = []
    p = re.compile('newinstr ')
    
    for line in csdx.splitlines():
        m = p.match(line)
        
        if m:
            try:
                c.append(definstr_dict.gen_instr(line))
            except:
                print '*error*'
                print '    template', get_newinstr_definstr(line), 'not defined'
                print '    line:', line
                print '    def do_instrs(csdx, definstr_dict):'
                exit()
                
        else:
            c.append(line)
            
    return '\n'.join(c)

def gen_alwayson_events(alwayson_list):
    '''Generates score events for a list of alwayson statements.'''
    
    events = []
    
    for e in alwayson_list:
        line = []
        line.append('i')
        line.append('"' + get_alwayson_name(e) +'"')
        line.append('0')
        line.append('-1')
        
        for a in get_alwayson_parameters(e):
            line.append(a)
            
        events.append(' '.join(line))
        
    return '\n'.join(events)    

def gen_newinstr(newinstr_statement, definstr_block, indent=4):
    '''Return a string of a new Csound instrument created from a
    template.'''
    
    body = string.Template(get_definstr_body(definstr_block))
    
    t = gen_template_dict(newinstr_statement,
                    get_definstr_args(get_definstr_statement(definstr_block)))

    instr = []
    instr.append(' '.join(['instr', get_newinstr_name(newinstr_statement)]))

    # Template substitution
    try:
        sub = body.substitute(t)
    except KeyError:
        print '*error*'
        print '    Template', get_newinstr_definstr(newinstr_statement),
        print 'is invalid due to an unrecognized key. Double check all',
        print '${} keys.'
        print '    block: ', newinstr_statement
        exit()
    
    # Indent body of instr
    for line in sub.splitlines():
        instr.append(''.join([' ' * indent, line]))
        
    instr.append('endin')
    instr.append('')
    
    return '\n'.join(instr)

def gen_template_dict(newinstr_statement, definstr_args):
    '''Generates a dict to use with a definstr template.'''
    
    newinstr_name = get_newinstr_name(newinstr_statement)
    newinstr_args = get_newinstr_args(newinstr_statement)
    num_required_args = get_num_pure_args(definstr_args)
    passed_pure_args = get_num_pure_args(newinstr_args)
    t = {}
    
    # Too many args?
    if len(newinstr_args) > len(definstr_args):
        try:
            raise Exception()
        except Exception:
            print '*error*'
            print '    Newinstr args exceed number of args in definstr.'
            print '    line:', newinstr_statement
            exit()

    # Not enough required args?
    if len(newinstr_args) < num_required_args:
        try:
            raise Exception()
        except Exception:
            print '*error*'
            print '    Too few newinstr args.'
            print '    line:', newinstr_statement
            exit()
    
    # Add reserved names
    t['name'] = newinstr_name
    #t['definstr'] = ???
    
    # Add pure args to template dict
    for i in range(passed_pure_args):        
        if not is_default_arg(definstr_args[i]):
            t[definstr_args[i]] = newinstr_args[i]
        else:
            m = re.match('(\w+)=(.+)', definstr_args[i])
            
            if m:
                t[m.group(1)] = newinstr_args[i]
    
    # Add default args to template dict
    if passed_pure_args < len(definstr_args):
        for a in newinstr_args[passed_pure_args:]:
            m = re.match('(\w+)=(.+)', a)
            
            if m:
                t[m.group(1)] = m.group(2)
    
    # Add unused default args to dict
    for a in definstr_args[passed_pure_args:]:
        m = re.match('(\w+)=(.+)', a)
        
        if m.group(1) not in t:
            t[m.group(1)] = m.group(2)
   
    return t
    
def get_alwayson_name(alwayson_statement):
    '''Returns the name of the instrument in an alwayson statement.'''
    
    m = re.match('alwayson\s+(\w+)', alwayson_statement )

    try:
        return m.group(1)
    except:
        exit('*Error* alwayson requires at least on arg')

def get_alwayson_parameters(alwayson_statement):
    '''Returns a list of parameters in an alwayson statement.'''
    
    m = re.match('alwayson\s+\w+\s*(,.+)', alwayson_statement)
    
    if m:
        args = m.group(1).replace(',', ' ')
        return args.split()
    else:
        return []

def get_definstr_args(definstr_statement):
    '''Returns a list of arg definitions.'''
    
    s = re.match('definstr\s+\w+,(.+)', definstr_statement)
    
    if s:
        a = s.group(1)
        a = a.replace(',', ' ')
        return a.split()
        
    return []

def get_definstr_body(definstr_block):
    '''Returns the body portion of a definstr block.'''
    b = []
    
    for line in definstr_block.splitlines()[1:-1]:
        b.append(line)
        
    return '\n'.join(b)
    
def get_definstr_name(definstr_statement):
    '''Returns the definition name of a definstr statement.'''
    
    return definstr_statement.split()[1].replace(',', '')
    
def get_definstr_statement(definstr_block):
    '''Returns the defintion statement of a definstr block.'''

    return definstr_block.splitlines()[0]

def get_newinstr_name(newinstr_statement):
    '''Returns the name given to the instance of the definstr.'''
    
    m = re.match('newinstr\s+(\w+)', newinstr_statement)
    
    if m:
        return m.group(1)
        
    return None
    
def get_newinstr_definstr(newinstr_statement):
    '''Returns the name of the definstr template.'''
    
    m = re.match('newinstr\s+\w+\s*,\s*(\w+)', newinstr_statement)
    
    if m:
        return m.group(1)
        
    return None
    
def get_newinstr_args(newinstr_statement):
    '''Returns a list of the newinstr args.'''

    s = re.match('newinstr\s+\w+,\s*\w+,(.+)', newinstr_statement)
    
    if s:
        a = s.group(1)
        a = a.replace(',', '')
        args = a.split()
        return args
        
    return []

def get_num_pure_args(args):
    '''Return the number of pure (non-optional) args in an list.
    
    Pure args are those with the assignment operator. (=)
    '''
    
    pure_args = 0
    
    for a in args:
        if not is_default_arg(a):
            pure_args += 1
            
    return pure_args

def import_definstr(import_statement):
    '''Imports a definstr template from an external file.
    
    import NameOfDefinstr, "file"
    import NameOfDefinstr, "file", NameSubstitution
    '''

    import_statement = import_statement.strip()
    m = re.match('import\s+(\w+)\s*,\s*\"(.+)\"', import_statement)
    m2 = re.match('import\s+\w+\s*,\s*\".+\"\s*,\s*(\w+)', import_statement)
    
    if m:
        definstr_name = m.group(1)
        path = m.group(2)
    else:
        print '*error*'
        print '    invalid import statement'
        print '    line:', import_statement
        exit()
    
    if m2:
        definstr_rename = m2.group(1)
    else:
        definstr_rename = definstr_name

    # Get and sanitize file
    content = strip_lines(read_file(path))

    # Find definstr from file
    s = re.search('(definstr\s+' + definstr_name + '[\s|,].*?enddef)', content, 
                  re.DOTALL)
    
    if s:
                
        definstr = s.group(1).replace(definstr_name, definstr_rename, 1)
        return definstr
    else:
        print '*error*'
        print '    template', definstr_name, 'does not exist in files', path
        exit()

def is_default_arg(definstr_arg):
    '''Checks for default assignment (=), and returns True if one is
    present.'''
    
    m = re.search('=', definstr_arg)
    
    if m:
        return True
        
    return False

def prepend_score(csdx, text):
    '''Adds text to the beginning of a score in a CSD file.'''
    
    return csdx.replace('<CsScore>\n', '<CsScore>\n' + text + '\n')

def read_file(filename):
    '''Returns the contents of a text file.'''
            
    # Open and get contents of file
    try:
        f = open(filename)
        content = ''.join(f)
        f.close()
    except:
        print '*error*'
        print '    file', filename, 'does not exist.'
        exit()
    
    return content

def strip_lines(string):
    '''Strips each individual line in a string.'''

    s = []

    for line in string.splitlines():
        s.append(line.strip())
        
    return '\n'.join(s)

    
class DefinstrDict:
    '''Stores definstr blocks.
    
    These definstr blocks can be used to generate instrs in a Csound
    orchestra with a newinstr statement.
    '''
    
    def __init__(self):
        self.d = {}
        
    def add(self, definstr_block):
        name = get_definstr_name(definstr_block)
        
        if name not in self.d:
            self.d[name] = definstr_block
            
        else:
            exit('*ERROR* definstr ' + name + ' already defined')

    def gen_instr(self, newinstr_statement):
        try:
            definstr = self.d.get(get_newinstr_definstr(newinstr_statement))
        except:
            print '*error*'
            print '    class DefinstrDict def gen_instr()'
            exit()
            
        return gen_newinstr(newinstr_statement, definstr)

    
def do_every_pass(csdx, every_pass):
    instr = []

    instr.append('instr 2')
    
    for line in every_pass:
        instr.append((' ' * 4) + line)
        
    instr.append('endin')
    instr.append('')
    
    i = '\n'.join(instr)

    tag = '</CsInstruments>'
    csdx = csdx.replace(tag, '\n' + i + tag, 1) 
    return csdx

def do_init_instr(csdx):
    i = 'instr 1\nendin\n'
    
    tag = '</CsInstruments>'
    csdx = csdx.replace(tag, '\n' + i + tag, 1) 
    return csdx
    
    
def do_pseudo_autochnmix(csdx, every_pass):
    '''Find, process and replace autochnmix statements.'''
    
    c = []
    for line in csdx.splitlines():
        s = re.match('\s*autochnmix\s+(.+)', line)
        
        if s:
            a = s.group(1).split(',')
            copy = []
            
            for b in a:
                copy.append(b.strip())
                
            a = copy
            c.append('    chnmix ' + a[0] + ', ' + a[1])
            every_pass.append('chnclear ' + a[1])
                
        else:
            c.append(line)
    
    return '\n'.join(c)

def write_csd(csd):
    '''Writes a csd file.'''
    
    pass

    

if __name__ == '__main__':
# $ python slipmat.py myFile.csdx
#     This should create a file myFile.csd

    # Get filename
    try:
        filename = sys.argv[1]
    except:
        exit('*Error* No filename specified')

    f, ext = os.path.splitext(filename)
    m = re.match('.csdx', ext)
    
    if not m:
        print '*error*'
        exit('Input file must have the extension .csdx')
    
    d = DefinstrDict()
    ep = []
    csdx = strip_lines(read_file(filename))        
    csdx = do_definstrs(csdx, d)
    csdx = do_imports(csdx, d)
    csdx = do_newinstrs(csdx, d)
    csdx = do_alwayson(csdx)
    csdx = do_pseudo_autochnmix(csdx, ep)
    csdx = do_init_instr(csdx)
    csdx = do_every_pass(csdx, ep)
    csdx = prepend_score(csdx, 'i 2 0 -1')

    # Write to csd
    out = f + '.csd'
    outfile = open(out, 'w')
    outfile.write(csdx)
    outfile.close()
    
    '''
    Csound needs:
        to warn if chn is accessed without being first defined
    '''

