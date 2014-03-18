#!/usr/bin/python
''' webapp.py

    Jeff Ondich, 4/6/12

    A sample showing a couple simple-minded techniques for presenting a web form,
    sanitizing user input, and displaying source code.

    The program does one of two things, depending on its CGI parameters.

    1. Display the blank form if neither animal nor badanimal has been specified, followed
       by links to the source files.

    2. Display the blank form plus animal results if either animal or badanimal has
       been specified, followed by links to the source files. (You might want to think
       about how to have the form in this case contain the text that the user entered
       rather than just the 
'''

import cgi

def sanitizeUserInput(s):
    ''' There are better ways to sanitize input than this, but this is a very
        simple example of the kind of thing you can do to protect your system
        from malicious user input. Unfortunately, this example turns "O'Neill"
        into "ONeill", among other things.
    '''
    charsToRemove = ';,\\/:\'"<>@'
    for ch in charsToRemove:
        s = s.replace(ch, '')
    return s

def getCGIParameters():
    ''' This function grabs the HTTP parameters we care about, sanitizes the
        user input, provides default values for each parameter is no parameter
        is provided by the incoming request, and returns the resulting values
        in a dictionary indexed by the parameter names ('animal' and 'badanimal'
        in this case).
    '''
    form = cgi.FieldStorage()
    parameters = {'animal':'', 'badanimal':'', 'showsource':''}

    if 'animal' in form:
        parameters['animal'] = sanitizeUserInput(form['animal'].value)

    if 'badanimal' in form:
        parameters['badanimal'] = sanitizeUserInput(form['badanimal'].value)

    return parameters

def printFileAsPlainText(fileName):
    ''' Prints to standard output the contents of the specified file, preceded
        by a "Content-type: text/plain" HTTP header.
    '''
    text = ''
    try:
        f = open(fileName)
        text = f.read()
        f.close()
    except Exception, e:
        pass

    print 'Content-type: text/plain\r\n\r\n',
    print text

def printMainPageAsHTML(animal, badAnimal, templateFileName):
    ''' Prints to standard output the main page for this web application, based on
        the specified template file and parameters. The content of the page is
        preceded by a "Content-type: text/html" HTTP header.
        
        Note that this function is quite awkward, since it assumes knowledge of the contents
        of the template (e.g. that the template contains four %s directives), etc. But
        it gives you a hint of the ways you might separate visual display details (i.e. the
        particulars of the HTML found in the template file) from computational results
        (in this case, the strings built up out of animal and badAnimal). 
    '''
    animalReport = ''
    if animal or badAnimal:
        animalReport = '<p>I like %ss, too.</p>\n' % (animal)
        animalReport += '<p>Also, %ss are gross.</p>\n' % (badAnimal)

    links = '<p><a href="showsource.py?source=webapp.py">webapp.py source</a></p>\n'
    links += '<p><a href="showsource.py?source=%s">%s source</a></p>\n' % (templateFileName, templateFileName)
    links += '<p><a href="showsource.py?source=showsource.py">the script we use for showing source</a></p>\n'
    
    outputText = ''
    try:
        f = open(templateFileName)
        templateText = f.read()
        f.close()
        outputText = templateText % (animal, badAnimal, animalReport, links)
    except Exception, e:
        outputText = 'Cannot read template file "%s".' % (templateFileName)

    print 'Content-type: text/html\r\n\r\n',
    print outputText

def main():
    parameters = getCGIParameters()
    printMainPageAsHTML(parameters['animal'], parameters['badanimal'], 'template.html')
        
if __name__ == '__main__':
    main()


