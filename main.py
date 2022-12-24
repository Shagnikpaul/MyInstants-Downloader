from PIL import Image
from playsound import playsound
import customtkinter
from bsoup_test import getPage, searchq
# Modes: system (default), light, dark
customtkinter.set_appearance_mode("System")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("blue")
import requests
import threading
import os
import tkinter
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1600x800")
app.winfo_toplevel().wm_title('MyInstants downloader and player.')
app.winfo_toplevel().iconbitmap('main.ico')
# Use CTkButton instead of tkinter Button

# button2 = customtkinter.CTkButton(
#     master=app, text="Hello World 2 !", command=button_function, fg_color="#000000")
# button3 = customtkinter.CTkButton(
#     master=app, text="Hello World 2 !", command=button_function, fg_color="#000000")
# button2.grid(row=1,column=1)
# button3.grid(row=1, column=2)

if os.path.exists('downloads'):
    pass
else:
    os.mkdir('downloads')


def defaultHeading():
    labelheading.configure(text="MyInstants Downloader and \n Player")

def download(obj):
    r = requests.get(obj['url'], stream=True)
    try:
        with open(f"downloads\{obj['title']}.mp3", "wb") as audio:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    audio.write(chunk)
        labelheading.configure(text=f"{obj['title']}.mp3 \n was downloaded....")
        labelheading.after(2000,defaultHeading)
    except OSError:
        t:str = obj['title']
        t = t.replace('@','_')
        t = t.replace('?', '_')
        t = t.replace('$', '_')
        t = t.replace('%', '_')
        t = t.replace('&', '_')
        t = t.replace('*', '_')
        t = t.replace('/', '_')
        t = t.replace('\\', '_')
        t = t.replace(':', '_')
        try:
            with open(f"downloads\{t}.mp3", "wb") as audio:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        audio.write(chunk)
            labelheading.configure(text = f"{obj['title']} \n was downloaded....")
            labelheading.after(2000, defaultHeading)
        except OSError:
            print('Critical Error 💀') 

l = getPage("1")
page_no:int=1
button_list=[]
search_results=[]

def search_builder(query:str):
    global search_results
    if len(search_results)>0:
        try:
         for h in search_results:
            h[0].destroy()
            h[1].destroy()
        except:
            print('ooooof')    
        print('Iwas done --------------------------------------------')
    search_results = []
    u = 4
    c = 2
    i = 0
    q = 0
    l = searchq(query=query)
    if len(l) == 0:
        label.configure(text = "No Results")
    else:
        label.configure(text = f'{len(l)} results found.')
        for k in l:
           def pl(x=q):
                threading.Thread(target=playsound, args=(
                l[x]['url'],), daemon=True).start()
                # threading.Thread(target=download, args=(k,), daemon=True).start() 
           def downlo(x=q):
            threading.Thread(target=download, args=(l[x],), daemon=True).start()
           
           bu = customtkinter.CTkButton(
               master=frame2, text=f"{k['title']}", fg_color="#000000", command=pl, width=20, compound="left")
           dw = customtkinter.CTkButton(
               master=frame2, text='', command=downlo, fg_color="#000000", width=5, image=my_image)
           search_results.append([bu,dw])
           bu.grid(row=u, column=c, pady=2, sticky='w')
           dw.grid(row=u, column=(c+1),padx=5)
           q += 1
           i += 1
           u+=1
           if i % 4 == 0:
             c += 2
             u = 4


def search():
    text = entry.get()
    if text == '':
       print('nah man')
    else:
        threading.Thread(target=search_builder, args=(entry.get(),), daemon=True).start()

def a(strd:str):
    global page_no
    page_no = page_no+1
    labelheading3.configure(text=f'Showing currently Page no. \n {page_no}')
    l = getPage(page_no)
    u=0
    for i in button_list:
        def pl(x=u):
          threading.Thread(target=playsound, args=(
              l[x]['url'],), daemon=True).start()
          # threading.Thread(target=download, args=(l[x],), daemon=True).start()

        def downlo(x=u):
           threading.Thread(target=download, args=(l[x],), daemon=True).start()
        i[0].configure(command = pl)
        i[0].configure(text=l[u]['title'])
        i[1].configure(command=downlo)
        u += 1 

def nextp():
    l = threading.Thread(target=a, args=('sd',), daemon=True).start()


def b(strd: str):
    global page_no
    if page_no == 1:
        return
    page_no = page_no-1
    labelheading3.configure(text=f'Showing currently Page no. \n {page_no}')
    l = getPage(page_no)
    u = 0
    for i in button_list:
        def pl(x=u):
          threading.Thread(target=playsound, args=(
              l[x]['url'],), daemon=True).start()
          # threading.Thread(target=download, args=(l[x],), daemon=True).start()

        def downlo(x=u):
         threading.Thread(target=download, args=(l[x],), daemon=True).start()
        i[0].configure(command=pl)
        i[0].configure(text=l[u]['title'])
        i[1].configure(command=downlo)
        u += 1


def prevp():
    l = threading.Thread(target=b, args=('sd',), daemon=True).start()


frame = customtkinter.CTkFrame(master=app,
                               corner_radius=10, width=1200, height=500, fg_color='#242424')
frame.place(relx=0.0, rely=0.0, anchor=tkinter.NW)

frame2 = customtkinter.CTkFrame(master=app,
                                corner_radius=10, width=1200, fg_color='#242424')
frame2.place(relx=0.0, rely=0.6,anchor=tkinter.NW)





my_font2 = customtkinter.CTkFont(family="Roboto", size=20)
labelheading = customtkinter.CTkLabel(master=app, text="MyInstants Downloader and \n Player",font=my_font2)
labelheading.place(relx=0.9, rely=0.1, anchor=tkinter.NE)

labelheading3 = customtkinter.CTkLabel(
    master=app, text="Showing currently Page no. \n 1", font=my_font2)
labelheading3.place(relx=0.9, rely=0.2, anchor=tkinter.NE)


my_image = customtkinter.CTkImage(light_image=Image.open("downloadicon.png"),
                                  dark_image=Image.open(
                                      "downloadicon.png"),
                                  size=(15, 15))
emoji = customtkinter.CTkImage(light_image=Image.open("flush.png"),
                                  dark_image=Image.open(
                                      "flush.png"),
                                  size=(60, 60))
labelheading2 = customtkinter.CTkLabel(
    master=app, text="\n\n\n\n\n Made with least effort by Shagnik Paul.", font=my_font2,image=emoji)
labelheading2.place(relx=0.95, rely=0.8, anchor=tkinter.NE)
k = 0
u = 1
w = 1
for i in l:
    def ply(x=k):
        # v.set_media(vlc.Media(l[x]['url'])) #set_media(vlc.Media(l[x]['url']))
        threading.Thread(target=playsound, args=(
            l[x]['url'],), daemon=True).start()
        # threading.Thread(target=download, args=(l[x],), daemon=True).start()
    def downlo(x=k):
        threading.Thread(target=download, args=(l[x],), daemon=True).start()
    button = customtkinter.CTkButton(
        master=frame, text=i['title'], command=ply, fg_color="#000000", width=10,compound="left")
    dbutton = customtkinter.CTkButton(
        master=frame, text='', command=downlo, fg_color="#000000", width=5, image=my_image)
    button_list.append([button,dbutton])
    button.grid(row=w, column=u, pady=1,sticky='w')
    dbutton.grid(row=w, column=(u+1),pady=1,padx=20)
    k = k+1;
    w = w +1;
    if k%15 == 0:
        u = u+2
        w = 1


prev_button = customtkinter.CTkButton(
    master=app, text="< PREV PAGE", command=prevp, fg_color="#000000",width=20)
prev_button.place(relx=0.8, rely=0.4, anchor=tkinter.NE)
next_button = customtkinter.CTkButton(
    master=app, text="NEXT PAGE >", command=nextp, fg_color="#000000", width=20)
next_button.place(relx=0.9, rely=0.4, anchor=tkinter.NE)
my_font = customtkinter.CTkFont(family="Roboto", size= 20)
label = customtkinter.CTkLabel(master=frame2, text="Search", compound="center",font=my_font)
label.grid(row=1, column=1)
entry = customtkinter.CTkEntry(master=frame2, placeholder_text="Search Query",)
entry.grid(row=2, column=1,pady=5)
search_button = customtkinter.CTkButton(
    master=frame2, text="Search", command=search, fg_color="#000000", width=100)
search_button.grid(row=3, column=1,pady=2)

def openDownload():
    os.startfile(os.getcwd()+'/downloads')

download_folder = customtkinter.CTkButton(master=app,text='Open downloads folder.',fg_color='#000000',command=openDownload)
download_folder.place(relx=0.87, rely=0.5, anchor=tkinter.NE)
threading.Thread(target=playsound, args=(
    'on.mp3',), daemon=True).start()

app.mainloop()
