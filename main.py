from helper import Helper
from tkinter import Label, Frame, Tk, StringVar


def get_data():
    helper = Helper()
    helper.load()
    return helper.get_users()


class tk_handler():
    root = Tk()
    data = None
    canvas_list = dict()
    frame_list = dict()
    pos_x, pos_y = 10, 10
    pos_y_increment = 20
    row = 1

    def __init__(self):
        self.root.wm_title("Internet Check")

        self.frame = Frame(self.root)
        self.frame.grid(row=0, column=4, sticky="n")

        Label(self.root, text="MAC").grid(row=0, column=0, sticky="nw")
        Label(self.root, text="DOWNLOAD").grid(row=0, column=1, sticky="nw")
        Label(self.root, text="DOWN SPEED").grid(row=0, column=2, sticky="nw")
        Label(self.root, text="UPLOAD").grid(row=0, column=3, sticky="nw")
        Label(self.root, text="UP SPEED").grid(row=0, column=4, sticky="nw")

        self.parse_data()

        self.root.mainloop()

    def create_frame(self):
        self.frame = Frame(self.root)
        self.frame.grid(row=0, column=4, sticky="n")

        Label(self.root, text="MAC").grid(row=0, column=0, sticky="nw")
        Label(self.root, text="DOWNLOAD").grid(row=0, column=1, sticky="nw")
        Label(self.root, text="DOWN SPEED").grid(row=0, column=2, sticky="nw")
        Label(self.root, text="UPLOAD").grid(row=0, column=3, sticky="nw")
        Label(self.root, text="UP SPEED").grid(row=0, column=4, sticky="nw")

    def update_row(self):
        self.row += 1
        self.frame.grid(row=self.row)

    def parse_data(self):
        self.data = get_data()
        for i in self.data:
            user = self.data[i]
            if i not in self.frame_list:
                var_mac = StringVar()
                var_download = StringVar()
                var_down_speed = StringVar()
                var_upload = StringVar()
                var_up_speed = StringVar()

                mac = Label(self.root, textvariable=var_mac)
                mac.grid(row=self.row, column=0, sticky="nw")

                download = Label(self.root, textvariable=var_download)
                download.grid(row=self.row, column=1, sticky="nw")

                down_speed = Label(self.root, textvariable=var_down_speed)
                down_speed.grid(row=self.row, column=2, sticky="nw")

                upload = Label(self.root, textvariable=var_upload)
                upload.grid(row=self.row, column=3, sticky="nw")

                up_speed = Label(self.root, textvariable=var_up_speed)
                up_speed.grid(row=self.row, column=4, sticky="nw")

                self.frame_list[i] = [
                    (mac, var_mac),
                    (download, var_download),
                    (down_speed, var_down_speed),
                    (upload, var_upload),
                    (up_speed, var_up_speed)
                ]

                self.update_row()
            else:
                self.frame_list[i][0][1].set(user.macaddress)
                self.frame_list[i][1][1].set(
                    self.parse_speed(user.download))
                self.frame_list[i][2][1].set(
                    self.parse_speed(user.download_speed))
                self.frame_list[i][3][1].set(
                    self.parse_speed(user.upload))
                self.frame_list[i][4][1].set(
                    self.parse_speed(user.upload_speed))

                color = 'red' if user.download_speed > 500 else 'black'

                for j in range(5):
                    self.frame_list[i][j][0].config(fg=color)

        self.root.after(1000, self.parse_data)

    def change_text(self):
        self.canvas.itemconfig(self.creature_text, text=self.name)
        self.root.after(2000, self.change_text)

    def parse_speed(self, speed):
        extension = " MB"
        speed = float(speed)/1024.0
        if speed > 1000.0:
            speed = speed/1024.0
            extension = " GB"

        speed = "{0:.2f}".format(speed)
        return speed + extension


if __name__ == '__main__':
    ttk = tk_handler()
