import pywinauto, time
from pywinauto.application import Application
from pywinauto.keyboard import send_keys

program_path = r"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe"
file_path = r"C:\Users\Sumits Acer\Downloads\33ZD_ GRATUITY NOMINATION.PDF"

app = Application(backend=u'uia').start(cmd_line='"'+program_path+'"' + ' ' + '"'+file_path+'"')
print("started")
time.sleep(1)
send_keys('^p')

w_handle = pywinauto.findwindows.find_window(title='Print')
time.sleep(1)
window=app.window(handle=w_handle)
window.wait('ready', timeout=10)

window[u'Printer:ComboBox'].select('OneNote (Desktop)')

print('Printer menu selected..')
window.Print.click()
print('PDF printed..')

