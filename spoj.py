from robobrowser import RoboBrowser
import os
extension = {"C++":"cpp","C":"c","C++14":"cpp","Java":"java","Python":"py"}
username = raw_input("Enter your spoj username:")
password = raw_input("Enter your spoj password:")
browser = RoboBrowser(parser = "html5lib")
browser.open('http://www.spoj.com/')
form = browser.get_form(id='login-form')
form['login_user'].value = username
form['password'].value = password
browser.submit_form(form)
browser.open('http://www.spoj.com/myaccount')
problems = browser.find(id = "user-profile-tables").find_all('td')
os.mkdir("spoj_solutions")
for problem in problems:
	link = problem.a['href']
	pname = problem.a.get_text()
	link = "http://www.spoj.com" + link
	browser.open(link)
	codelink = "http://www.spoj.com" + browser.find(title = 'Edit source code')['href']
	codelang = browser.find(class_ = 'slang text-center').get_text().split(' ')[0].strip()
	browser.open(codelink)
	f = open("./spoj_solutions/%s.%s"%(pname,extension[codelang]),"w")
	f.write(str(browser.find(id = 'submit_form').textarea.get_text()))
	f.close()

