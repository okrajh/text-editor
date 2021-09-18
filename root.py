import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog, messagebox
import os
main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('Vpad Text Editor')

#>>>>>>>>>>>>>>>>>  (1)MAIN MENU   <<<<<<<<<<<<<<
main_menu = tk.Menu()

# THIS IS FILE MENU

file = tk.Menu(main_menu, tearoff = False)
main_menu.add_cascade(label='File',menu =file ) #cascade in main_menu
            #assign icons for file menu
new_icon = tk.PhotoImage(file='icons2/new.png')
open_icon = tk.PhotoImage(file='icons2/open.png')
save_icon = tk.PhotoImage(file='icons2/save.png')
save_as_icon = tk.PhotoImage(file='icons2/save_as.png')
exit_icon = tk.PhotoImage(file='icons2/exit.png')


#THIS IS EDIT MENU

edit = tk.Menu(main_menu, tearoff = False)
main_menu.add_cascade(label='Edit', menu =edit) #cascade in main_menu
              # assign icons for edit menu
copy_icon = tk.PhotoImage(file='icons2/copy.png')
past_icon = tk.PhotoImage(file='icons2/paste.png')
cut_icon = tk.PhotoImage(file='icons2/cut.png')
clear_all_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon = tk.PhotoImage(file='icons2/find.png')
 

#THIS IS VIEW MENU 
view = tk.Menu(main_menu, tearoff = False)
main_menu.add_cascade(label='View', menu= view) #cascade in main_menu
                 #ASSING ICON for view menu
tool_bar_icon = tk.PhotoImage(file='icons2/tool_bar.png')
status_icon = tk.PhotoImage(file='icons2/status_bar.png')


#THIS THEME MENU

color_theme = tk.Menu(main_menu, tearoff = False)
main_menu.add_cascade(label='Color Theme', menu =color_theme)
                #assign icon for theme
light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')

                    #theme choice variable
theme_choice = tk.StringVar()
color_icon =(light_default_icon,light_plus_icon,dark_icon,monokai_icon,night_blue_icon)
                    #color dictinary
color_dict ={
        'Light Default':('#000000','#ffffff'),
        'Light Plus':('#000000','#AEB6BF'),
        'Dark':('#F7F9F9','#212F3D'),
        'Monokai':('#F4F6F6','#239B56'),
        'Night Blue':('#3498DB','#2874A6')
}

#>>>>>>>>>>>>>>>>>  MAIN MENU END  <<<<<<<<<<<


#>>>>>>>>>>>>>>>>>  (2)tool bar   <<<<<<<<<<<<<<
                    #tool Bar label
tool_bar = ttk.Label(main_application)
tool_bar.pack(side = tk.TOP, fill=tk.X)

                    #font faimly assign in touple
font_touple = tk.font.families()
                    #font change combobox
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar,width = 30, textvariable = font_family, state='readonly')
font_box['values'] = font_touple
font_box.current(font_touple.index('Arial'))
font_box.grid(row = 0, column = 0, padx =5)

                     #font_size combobox
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar,width = 14, textvariable = size_var, state='readonly')
font_size['values'] = tuple(range(8,80,2))
font_size.current(3)
font_size.grid(row=0, column =1, padx = 5)


                    #bold ,italic ,underline button

bold_icon = tk.PhotoImage(file='icons2/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row= 0, column =2,padx =4)

italic_icon = tk.PhotoImage(file='icons2/italic.png')
italic_btn = tk.Button(tool_bar, image = italic_icon)
italic_btn.grid(row =0, column = 3, padx =4)

underline_icon = tk.PhotoImage(file='icons2/underline.png')
uderline_btn = tk.Button(tool_bar, image = underline_icon)
uderline_btn.grid(row =0  ,column =4)

                    #font color button
font_color_icon = tk.PhotoImage(file ='icons2/font_color.png')
font_color_btn = ttk.Button(tool_bar, image = font_color_icon)
font_color_btn.grid(row = 0, column =5, padx =5)

                    #align left,rigth,center icon
align_left_icon = tk.PhotoImage(file='icons2/align_left.png')
align_left_btn = ttk.Button(tool_bar, image = align_left_icon)
align_left_btn.grid(row = 0, column = 6, padx =5)

align_center_icon = tk.PhotoImage(file='icons2/align_center.png')
align_center_btn = tk.Button(tool_bar, image = align_center_icon)
align_center_btn.grid(row = 0, column = 7 ,padx =5)

align_right_icon = tk.PhotoImage(file='icons2/align_right.png')
align_right_btn = ttk.Button(tool_bar, image = align_right_icon)
align_right_btn.grid(row = 0 , column =8, padx =5)


#>>>>>>>>>>>>>>>>>  tool bar END  <<<<<<<<<<<<<<<<<<<<<<<<<



#>>>>>>>>>>>>>>>>>  (3)text editor   <<<<<<<<<<<<<<<<<<<<<<<<
text_editor = tk.Text(main_application)
text_editor.config(wrap ='word', relief = tk.FLAT)
text_editor.focus_set()
scroll_bar = tk.Scrollbar(main_application)
scroll_bar.pack(side = tk.RIGHT, fill = tk.Y)
text_editor.pack(fill = tk.BOTH, expand = True)
scroll_bar.config(command = text_editor.yview)
text_editor.config(yscrollcommand = scroll_bar.set)


                    #fuctionality of textEditor

#font family and font size functionality
current_font_family = 'Arial'
current_font_size = 14

def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))

def change_fontsize(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))

#bind combobox with function (change_font)

font_box.bind("<<ComboboxSelected>>",change_font)

#bind combobox with function (change_font_size)
font_size.bind("<<ComboboxSelected>>",change_fontsize)

#text editor configure for type Arial ,and font size 12
text_editor.configure(font =('Arial',14))

                               #button functionality

#bold button functionality
def change_bold():
        text_property = tk.font.Font(font=text_editor['font'])
        if text_property.actual()['weight'] == 'normal':
            text_editor.configure(font = (current_font_family, current_font_size, 'bold'))
        if text_property.actual()['weight'] == 'bold':
            text_editor.configure(font = (current_font_family,current_font_size,'normal'))

bold_btn.configure(command = change_bold)

#italic button functionality
def change_italic():
        text_property = tk.font.Font(font=text_editor['font'])
        if text_property.actual()['slant'] == 'italic':
            text_editor.configure(font = (current_font_family, current_font_size, 'roman'))
        if text_property.actual()['slant'] == 'roman':
            text_editor.configure(font = (current_font_family,current_font_size,'italic'))

italic_btn.configure(command = change_italic)

def change_underline():
        text_property = tk.font.Font(font=text_editor['font'])
        if text_property.actual()['underline'] == 0:
            text_editor.configure(font = (current_font_family, current_font_size, 'underline'))
        if text_property.actual()['underline'] == 1:
            text_editor.configure(font = (current_font_family,current_font_size,'normal'))
uderline_btn.configure(command = change_underline)


def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg = color_var[1])

font_color_btn.configure(command = change_font_color)

            # alignment functionality


def align_left():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify = tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content,'left')
align_left_btn.configure(command = align_left)

def align_center():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify = tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content,'center')
align_center_btn.configure(command = align_center)

def align_right():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify = tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content,'right')
align_right_btn.configure(command = align_right)

#status bar
text_changed = False
def changed(event = None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0,'end-1c').replace(' ',''))
        status_bar.config(text = f'characters: {characters} Words: {words}')
    text_editor.edit_modified(False)
text_editor.bind('<<Modified>>', changed)
#>>>>>>>>>>>>>>>>>  text editor end    <<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>  (4)main status bar   <<<<<<<<<<<<<<
status_bar = ttk.Label(main_application, text = 'status bar')
status_bar.pack(side = tk.BOTTOM)


#>>>>>>>>>>>>>>>>> main status bar end <<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>> (5)main menu functionality  <<<<<<<<<<<<<<
# variable
url = ''

#new funtionality
def new_file(event = None):
    global url
    url = ''
    text_editor.delete(1.0,tk.END)

#open functionality
def open_file(event = None):
    global url
    url =filedialog.askopenfilename(initialdir = os.getcwd(),title ='Select file',filetypes =(('Text File','*.txt'),('All files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
            return
    except:
        return
    main_application.title(os.path.basename(url))
       
#save functionlaity
def save_file(event = None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url, 'w',encoding= 'utf-8') as fw:
                fw.write(content)
        else:
            url =filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt',filetypes =(('Text File','*.txt'),('All files','*.*')))    
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
            return
#save as functionality

def save_as(event= None):
    global url
    try:
        content = text_editor.get(1.0,tk.END)
        url =filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt',filetypes =(('Text File','*.txt'),('All files','*.*')))
        url.write(content)
        url.close()
    except:
        return

#exit functionality
def exit_func(event = None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning','Do you want to save thr file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url,'w', encoding= 'utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0,tk.END))
                    url =filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt',filetypes =(('Text File','*.txt'),('All files','*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()

        else:
            main_application.destroy()
    except:
        return


#edit functionality
# Find Functionality  
def find_func(event = None):
    find_dialog = tk.Toplevel()
    find_dialog.geometry('450x250+500+200')
    find_dialog.title('Find')
    find_dialog.resizable(0,0)
    
    #find
    def find():
        word = find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex= tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches +=1
                start_pos = end_pos
                text_editor.tag_config('match', foreground ='red', background = 'yellow')
    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0,new_content)

#
                ###Frame
    find_frame = ttk.LabelFrame(find_dialog,text ='Find/Replace')
    find_frame.pack(pady = 40)
     ##labels
    text_find_label = ttk.Label(find_frame,text ='find')
    text_replace_label = ttk.Label(find_frame, text ='Replace')
    ##entry box
    find_input = ttk.Entry(find_frame, width = 30)
    replace_input = ttk.Entry(find_frame, width = 30)
    ##botton
    find_button  = ttk.Button(find_frame, text= 'find' ,command = find)
    replace_button = ttk.Button(find_frame, text= 'Replace', command = replace)

    ##Grid Label
    text_find_label.grid(row = 0 , column = 0, padx =4, pady = 4)
    text_replace_label.grid(row = 1 , column = 0, padx =4, pady = 4)
    ## grid entry box
    find_input.grid(row=0,column=1,padx=4, pady =4)
    replace_input.grid(row=1,column=1,padx=4, pady =4)
    ## button grid
    find_button.grid(row=0,column=3,padx=8, pady =4)
    replace_button.grid(row =1, column =3, padx=8, pady =4)

    find_dialog.mainloop()
            #add commands in file menu (drop down)
file.add_command(label='New',image = new_icon ,compound =tk.LEFT,accelerator='ctrl+N' , command= new_file)
file.add_command(label='Open',image = open_icon ,compound =tk.LEFT,accelerator='ctrl+O', command = open_file)
file.add_command(label='Save',image = save_icon ,compound =tk.LEFT,accelerator='ctrl+S' ,command = save_file)
file.add_command(label='Save as',image = save_as_icon ,compound =tk.LEFT,accelerator='ctrl+Alt+S' , command = save_as)
file.add_command(label='Exit',image = exit_icon ,compound =tk.LEFT,accelerator='ctrl+Q' , command= exit_func)
             #add command in edit menu (drop down for edit)
edit.add_command(label='Copy',image = copy_icon ,compound =tk.LEFT,accelerator='ctrl+C', command = lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Past',image = past_icon ,compound =tk.LEFT,accelerator='ctrl+V', command = lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut',image = cut_icon ,compound =tk.LEFT,accelerator='ctrl+X',  command = lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear all',image = clear_all_icon ,compound =tk.LEFT , command = lambda:text_editor.delete(1.0,tk.END))
edit.add_command(label='Find',image = find_icon,compound =tk.LEFT,accelerator='ctrl+H',command = find_func)
                #ADD CHECK BUTTON



##veiw button functionality
 
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side = tk.TOP, fill = tk.X)
        text_editor.pack(fill = tk.BOTH, expand = True)
        status_bar.pack(side = tk.BOTTOM)
     
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side = tk.BOTTOM)
        show_statusbar = True
view.add_checkbutton(label='Tool bar', onvalue = True ,offvalue = False,image= tool_bar_icon, compound=tk.LEFT,variable = show_toolbar ,command = hide_toolbar )
view.add_checkbutton(label ='Status bar',onvalue = 1, offvalue =False, image = status_icon, compound=tk.LEFT,variable = show_statusbar, command = hide_statusbar)

#color theme
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color = color_tuple[0]
    bg_color = color_tuple[1]
    text_editor.config(background = bg_color,fg = fg_color)


                #for loop for creat radio button
count = 0
for i in color_dict:
    color_theme.add_radiobutton(label = i, image =color_icon[count],variable = theme_choice, compound= tk.LEFT, command = change_theme)
    count+=1

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<
#BIND  SHORT-CUT KEYS
main_application.bind("<Control-n>" ,new_file)
main_application.bind("<Control-o>" ,open_file)
main_application.bind("<Control-s>" ,save_file)
main_application.bind("<Control-Alt-s>" ,save_as)
main_application.bind("<Control-q>" ,exit_func)
main_application.bind("<Control-f>",find_func)

 
#>>>>>>>>>>>>>>>>> main menu functionality end  <<<<<<<<<<<<<<
main_application.config(menu = main_menu)
main_application.mainloop()
