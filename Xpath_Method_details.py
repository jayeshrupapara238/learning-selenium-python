'''
type of the xpath

1. Absolute xpath: It contain the complete path from root element of page to desired element
- Absolute x path start with root node. single forword slash(/)
- Drawback with Absolute xpath is slighly changes in DOM makes a xpath invalid

Xpath = //root/middle//Tagname[@Attribute='Value']

2. Relative xpath: In ralative xpath, xpath start with middle of the html DOM
- start with dobule forword slash(//)
- advantage is it's less brittle

Xpath = //Tagname[@Attribute='Value']


'''


'''
1.Xpath function start-with

Apath = //tagname[start-with(@Attribute,'Value')]

'''


'''
2.Xpath function Contains

Xpath = //tagname[contains(@Attribute,'value')]
'''


'''
3.Xpath test() method

Xpath = //tagname(text()='ActualText')

'''

'''
4.Xpath AND and OR operator


Xpath = //Tagname[@Attribute='Value' or @Atrribute='Value']
Xpath = //Tagname[@Attribute='Value' and @Attribute='Value']

'''

'''
5. Xpath Axes Methods (parent/child/self)

Xpath = //tagname[@Attribute='vlaue']//parent::tagname
Xpath = //tagname[@Attribute='Vlaue']//child::tagname
Xpath = //tagname[@Attribute='Value']//self::tagname

'''

'''
6. Xpath Axes Method (descendant/descendant-or-self)

Xpath = //Tagname[@Attribuute='value']//descedant::Tagname
Xpath = //Tagname[@Attribute='Value']//descendant-or-self::tagname

'''

'''
7. Xpath Axes Method (ancestor/ancestor-or-self)

Xpath = //tagname[@Attribute='Value']//ancestor::tagname
Xpath = //tagname[@Attribute='value']//ancestor-or-self::tagname

'''

'''
8. Xpath Axes Method (following/ following-sibling)

Xpath = @tagname[@Attribute='Value']//following::tagname
Xpath = @tagname[@Attribute='Value']//following-sibling::tagname

'''

'''
9. Xpath Axes Method (preceding/preceding-sibling)

Xpath = @tagname[@Attribute='Value']//preceding::tagname
Xpath = @tagname[@Attribute='value']//preceding-sibling::tagname

'''


'''
selectorshub - Google chrome plugin to get support to get reletive XPath

'''