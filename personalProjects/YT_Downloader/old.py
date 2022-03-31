import wx
import validators
from pytube import YouTube

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MyFrame, self).__init__(size=(800, 600), *args, **kwargs)
        self.panel = wx.Panel(self, style=wx.BORDER_SUNKEN)
        self.url = None
        self.downloadPath = None
        self.SetUpGUI()
        self.resolutions = ["1080p", "720p", "480", "360p", "240p"]

    def SetUpGUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.AddStretchSpacer()

        label = wx.StaticText(self.panel, label="YouTube Downloader", style=wx.ALIGN_CENTRE_HORIZONTAL, size=(250, -1))
        label.SetFont(wx.Font(wx.FontInfo(20)))

        row1 = wx.BoxSizer(wx.VERTICAL)
        self.url = wx.TextCtrl(self.panel, -1, style=wx.TE_CENTRE, size=(800, 25), pos=(10, 10))
        vbox.Add(label, 0, wx.CENTER)
        vbox.Add(self.url, 0, wx.CENTER)

        row2 = wx.BoxSizer(wx.HORIZONTAL)
        self.downloadPath = wx.TextCtrl(self.panel, -1, style=wx.TE_CENTRE, size=(700, 25), pos=(10, 10))
        browse = wx.Button(self.panel, label='Browse')
        browse.Bind(wx.EVT_BUTTON, self.browseFolders)
        row2.Add(self.downloadPath, 0)
        row2.Add(browse, 0)

        download_BTN = wx.Button(self.panel, label='Download', style=wx.ALIGN_CENTER)
        download_BTN.Bind(wx.EVT_BUTTON, self.downloadVideo)


        vbox.Add(row1, 0, wx.CENTER)
        vbox.Add(row2, 0, wx.CENTER)
        vbox.Add(download_BTN, 0, wx.CENTER)
        vbox.AddStretchSpacer()
        self.panel.SetSizer(vbox)

        self.Show()

    def browseFolders(self, *args):
        download_dir = wx.DirDialog(self.panel, style=wx.DD_DEFAULT_STYLE)
        download_dir.ShowModal()
        self.downloadPath.Value = download_dir.GetPath()
        print(download_dir.GetPath())

    def downloadVideo(self, *args):
        vidLink = self.url.Value
        print(vidLink)

        if not validators.url(self.url.Value):
            print('invalid url')
        else:
            folder = self.downloadPath.Value
            get_video = YouTube(vidLink)
            get_stream = self.getQualityStream(get_video)
            print(get_stream)
            get_stream.download(folder)
            wx.MessageDialog(self.panel, message=("Video was successfully downloaded. The file can be found" 
                                                  " at "+self.downloadPath.Value)).ShowModal()

    def getQualityStream(self, link):
        for reso in self.resolutions:
            streams = link.streams.filter(res=reso, progressive=True)
            if len(streams) != 0:
                return streams.first()

def main():
    app = wx.App()
    MyFrame(None, title="DownloadYT")
    app.MainLoop()


if __name__ == "__main__":
    main()
