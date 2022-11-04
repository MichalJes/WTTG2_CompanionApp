import wx
import time
import winsound
import threading


class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(500, 500))

        self.InitUI()
        self.Centre(wx.BOTH)
        self.Show()

    def InitUI(self):

        panel = wx.Panel(self)
        grid_sizer = wx.GridSizer(3, 2, 5, 5)

        Timer1_btn = wx.Button(panel, label='TPLINK_8907_5G')
        Timer2_btn = wx.Button(panel, label='DDW35363')
        Timer3_btn = wx.Button(panel, label='TC8717T10')
        Timer4_btn = wx.Button(panel, label='doody')
        Timer5_btn = wx.Button(panel, label='FreeWifiNoVirus')

        grid_sizer.AddMany([(Timer1_btn, 0, wx.EXPAND),
                            (Timer2_btn, 0, wx.EXPAND),
                            (Timer3_btn, 0, wx.EXPAND),
                            (Timer4_btn, 0, wx.EXPAND),
                            (Timer5_btn, 0, wx.EXPAND), ])

        Timer1_btn.Bind(wx.EVT_BUTTON, self.StartTimer, Timer1_btn)
        Timer2_btn.Bind(wx.EVT_BUTTON, self.StartTimer, Timer2_btn)
        Timer3_btn.Bind(wx.EVT_BUTTON, self.StartTimer, Timer3_btn)
        Timer4_btn.Bind(wx.EVT_BUTTON, self.StartTimer, Timer4_btn)
        Timer5_btn.Bind(wx.EVT_BUTTON, self.StartTimer, Timer5_btn)

        panel.SetSizer(grid_sizer)

    def StartTimer(self, event):
        btn_label = event.GetEventObject().GetLabel()
        match btn_label:
            case "TPLINK_8907_5G":
                wifi_time = 960
            case "DDW35363":
                wifi_time = 480
            case "TC8717T10":
                wifi_time = 420
            case "doody":
                wifi_time = 630
            case "FreeWifiNoVirus":
                wifi_time = 300

        progressDialog = ProgressFrame(None, btn_label, wifi_time)
        progressDialog.Show()
        # progressDialog.StartTimer(wifi_time)
        self.StartThread(progressDialog.StartTimer, wifi_time)

    def StartThread(self,function, wifi_time):
        new_thread = threading.Thread(target=function, args=[wifi_time])
        new_thread.start()
        # new_thread.join()


class ProgressFrame(wx.Frame):
    def __init__(self, parent, title, wifi_time):
        super().__init__(parent, title=title, size=(200, 200))
        self.InitUI(wifi_time)
        self.Centre(wx.BOTH)
        self.Show()

    def BEEP(iterations, event):
        while iterations > 0:
            winsound.Beep(2000, 200)
            time.sleep(0.1)
            iterations -= 1

    def BEEPlong(iterations, event):
        while iterations > 0:
            winsound.Beep(2000, 800)
            time.sleep(0.1)
            iterations -= 1

    def InitUI(self, wifi_time):
        panel = wx.Panel(self)
        box_sizer = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)

        self.gauge = wx.Gauge(panel, range=wifi_time, size=(
            250, 20), style=wx.GA_HORIZONTAL)
        self.message = wx.TextCtrl(
            panel, value="Test text", style=wx.TE_READONLY | wx.TE_CENTER)
        self.cancel_btn = wx.Button(panel, label="Cancel timer")
        self.cancel_btn.Bind(wx.EVT_BUTTON, self.OnClose)

        hbox1.Add(self.gauge, proportion=1, flag=wx.ALIGN_CENTRE)
        hbox2.Add(self.message, proportion=1, flag=wx.ALIGN_CENTRE)
        hbox3.Add(self.cancel_btn, proportion=1, flag=wx.ALIGN_CENTRE)

        box_sizer.Add((0, 30))
        box_sizer.Add(hbox1, flag=wx.ALIGN_CENTRE)
        box_sizer.Add((0, 20))
        box_sizer.Add(hbox2, proportion=1, flag=wx.ALIGN_CENTRE)
        box_sizer.Add((0, 20))
        box_sizer.Add(hbox3, flag=wx.ALIGN_CENTRE)
        panel.SetSizer(box_sizer)

        self.SetSize((300, 200))

    def OnClose(self, event):
        self.Close()

    def StartTimer(self, wifi_time):
        self.i = wifi_time
        for i in range(wifi_time, -1, -1):
            self.gauge.SetValue(self.i)
            self.message.SetValue(str(self.i)+" seconds left")
            if self.i == 120:
                self.BEEP(2)
            elif self.i == 0:
                self.BEEP(3)
                self.BEEPlong(1)
                return
            # self.progressDialog.Show()
            time.sleep(0.05)


if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame(None, title='WTTG2 WIFI timer')
    app.MainLoop()
