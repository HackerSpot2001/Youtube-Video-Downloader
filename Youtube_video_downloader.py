from tkinter import Label,Frame,Button,Entry,StringVar,Tk,TOP,X
from tkinter.messagebox import showwarning,showinfo
from tkinter import filedialog
from pytube import YouTube


def downloadvideo():
    download_button.configure(text="Downloding...")
    url_of_video = url_vid.get()
    url_of_video = str(url_of_video)
    if url_of_video == "":
        showwarning("Youtube Downloader","Please Enter Url")
    if url_of_video != "":
        filename_video = filedialog.askdirectory()
        if filename_video is None:
            return

        obj = YouTube(url_of_video)
        strem = obj.streams.first()
        strem.download(filename_video)
        showinfo("Download Video","The Youtube has been Downloaded in this path \n {}".format(filename_video))
        download_button.configure(text="Download Video")
        url_vid.set("")

if __name__ == "__main__":
    root = Tk()
    root.geometry("640x400+300+100")
    root.minsize(640,400)
    # root.maxsize(640,480)
    root.configure(bg="#B5AFAE")

    frame_youtube = Frame(root,bg="grey")
    frame_youtube.pack(side=TOP,fill=X,pady=20)
    label_youtube = Label(frame_youtube,text="Youtube Downloader",font=("sans-serif",25,'bold','italic'),bg="grey",fg="black",padx=10,pady=5)
    label_youtube.pack()

    url_vid = StringVar()
    url_vid.set("")

    frame_url= Frame(root,bg="#B5AFAE")
    frame_url.pack(fill=X,pady=20)
    url_label = Label(frame_url,text="Enter URL : ",bg="#B5AFAE",font=("sans-serif",15,'bold'))
    url_label.pack(pady=5)
    url_entry = Entry(frame_url,textvariable=url_vid,width=60,font=("sans-serif",13,'bold'))
    url_entry.pack(pady=5,ipady=3)


    frame_download = Frame(root,bg="#B5AFAE")
    frame_download.pack(fill=X,pady=20)
    download_button = Button(frame_download,text="Download Video",bg="grey",fg="white",font=("sans-serif",15,'bold'),command=downloadvideo)
    download_button.pack()
    root.mainloop()