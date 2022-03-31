import wx
import validators
from pytube import YouTube

class MainFrame(wx.Frame):
    # Constructor
    def __init__(self, *args, **kwargs):
        super(MainFrame, self).__init__(*args, **kwargs, size=(800, 600))

        #Properties
        self.screen_ = wx.Panel(self, style=wx.BORDER_SUNKEN)  # Main screen for app
        self.url_ = None  # link to YouTube video
        self.downloadPath_ = None  # Destination for video
        self.resolutions_ = ["1080p", "720p", "480", "360p", "240p"]  # Available resolutions

        self.SetUpGUI()  # Initiates the GUI

    def SetUpGUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.AddStretchSpacer()

        row1 = wx.BoxSizer(wx.HORIZONTAL)
        row2 = wx.BoxSizer(wx.HORIZONTAL)

        #App Title
        title = wx.StaticText(self.screen_, label="YouTube Downloader", style=wx.ALIGN_CENTER_HORIZONTAL, size=(250,
                                                                                                                -1))
        title.SetFont(wx.Font(wx.FontInfo(20)))
        vbox.Add(title, 0, wx.CENTER)

        #Everything in row 1
        label1 = wx.StaticText(self.screen_, label="URL:", style=wx.ALIGN_CENTER_HORIZONTAL)
        row1.Add(label1, 0, wx.CENTER)

        self.url_ = wx.TextCtrl(self.screen_, -1, style=wx.TE_CENTRE, size=(600, 25), pos=(10, 10))
        row1.Add(self.url_, 0, wx.CENTER)
        vbox.Add(row1, 0, wx.CENTER)

        #Everything in row 2
        label2 = wx.StaticText(self.screen_, label="Path:", style=wx.ALIGN_LEFT)
        row2.Add(label2, 0, wx.LEFT)

        self.downloadPath_ = wx.TextCtrl(self.screen_, -1, style=wx.TE_CENTRE, size=(514, 25), pos=(10, 10))
        row2.Add(self.downloadPath_, 0, wx.CENTER)

        browseBTN = wx.Button(self.screen_, label='Browse')
        browseBTN.Bind(wx.EVT_BUTTON, self.browseFolders)
        row2.Add(browseBTN, 0, wx.CENTER)
        vbox.Add(row2, 0, wx.CENTER)

        #Download Button
        downloadBTN = wx.Button(self.screen_, label='Download', style=wx.ALIGN_CENTER)
        downloadBTN.Bind(wx.EVT_BUTTON, self.downloadVideo)
        vbox.Add(downloadBTN, 0, wx.CENTER)

        vbox.AddStretchSpacer()
        self.screen_.SetSizer(vbox)
        self.Show()

    def browseFolders(self, *args):
        download_dir = wx.DirDialog(self.screen_, style=wx.DD_DEFAULT_STYLE)
        download_dir.ShowModal()
        self.downloadPath_.Value = download_dir.GetPath()

    def downloadVideo(self, *args):
        vidLink = self.url_.Value

        if not validators.url(self.url_.Value):
            print('invalid url')
        else:
            folder = self.downloadPath_.Value
            get_video = YouTube(vidLink)
            get_stream = self.getQualityStream(get_video)
            get_stream.download(folder)
            wx.MessageDialog(self.screen_, message=("Video was successfully downloaded. The file can be found"
                                                  " at " + self.downloadPath_.Value)).ShowModal()

    def getQualityStream(self, link):
        for reso in self.resolutions_:
            streams = link.streams.filter(res=reso, progressive=True)
            if len(streams) != 0:
                return streams.first()

def main():
    app = wx.App()
    MainFrame(None, title="YouTube Downloader")
    app.MainLoop()


if __name__ == "__main__":
    main()