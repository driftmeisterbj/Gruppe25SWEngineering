import wx

class ConnectToDevice(wx.Frame):
    def __init__(self, *args, **kw):
        super(ConnectToDevice, self).__init__(*args, **kw)

        # Sett opp vinduet
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        # Lag en liste over IoT-enheter som kan velges
        devices = ["Dørlås", "Termostat", "Babycall", "Kjøleskap"]

        # Lag en tekst som instruksjon
        instruction = wx.StaticText(panel, label="Velg en enhet fra listen:", pos=(10, 10))

        # Lag en listeboks for enheter
        self.device_list = wx.ListBox(panel, choices=devices, pos=(10, 40), size=(200, 100))

        # Koble hendelse til når en enhet velges
        self.device_list.Bind(wx.EVT_LISTBOX, self.on_device_selected)

        # Sett opp vinduet
        self.SetSize((300, 200))
        self.SetTitle('Tilkobling av enhet')
        self.Centre()
        self.Show(True)

    def on_device_selected(self, event):
        # Hent valgt enhet
        selected_device = self.device_list.GetStringSelection()
        wx.MessageBox(f'Du valgte {selected_device}', 'Enhet valgt', wx.OK | wx.ICON_INFORMATION)

def main():
    app = wx.App()
    ConnectToDevice(None)
    app.MainLoop()

if __name__ == '__main__':
    main()