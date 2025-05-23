import pandas as pd
import os
from tkinter import *
import customtkinter
from PIL import Image, ImageTk
from customtkinter import CTkImage
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import customtkinter
customtkinter.deactivate_automatic_dpi_awareness()

# Path Image
root_directory = os.path.dirname(os.path.abspath(__file__))
material_folder = os.path.join(root_directory, "Material")

img_path_hover1 = os.path.join(material_folder, "image_hover1.png")
img_path_center = os.path.join(material_folder, "image_1.png")
img_path_center2 = os.path.join(material_folder, "image_2.png")
img_path_center3 = os.path.join(material_folder, "image_3.png")
img_path_center4 = os.path.join(material_folder, "image_4.png")
img_path_center5 = os.path.join(material_folder, "image_5.png")
img_path_center6 = os.path.join(material_folder, "image_6.png")
img_path_center7 = os.path.join(material_folder, "image_7.png")
img_path_center8 = os.path.join(material_folder, "image_8.png")
img_path_center9 = os.path.join(material_folder, "image_9.png")
img_path_center10 = os.path.join(material_folder, "image_10.png")
img_path_center11 = os.path.join(material_folder, "image_11.png")
img_path_center12 = os.path.join(material_folder, "image_12.png")
img_path_center13 = os.path.join(material_folder, "image_13.png")
img_path_center14 = os.path.join(material_folder, "image_14.png")
img_path_center15 = os.path.join(material_folder, "image_15.png")
img_path_centerCR = os.path.join(material_folder, "image_crossRed.png")
img_path_hoverHR = os.path.join(material_folder, "image_hoverRed.png")
img_path_centerRP = os.path.join(material_folder, "image_RP.png")
img_path_centerHOME = os.path.join(material_folder, "image_home.png")

# Variable Answers
answers_fisikGenetikaGlukosa = {
    'question1': 0,
    'question2': 0,
    'question3': 0,
    'question4': 0,
    'question5': 0,
    'question6': 0,
    'question7': 0,
}

answers_gejala = {
    'gejala1': 0,
    'gejala2': 0,
    'gejala3': 0,
    'gejala4': 0,
    'gejala5': 0,
    'gejala6': 0,
    'gejala7': 0,
    'gejala8': 0,
    'gejala9': 0,
    'gejala10': 0,
    'gejala11': 0,
    'gejala12': 0,
    'gejala13': 0,
    'gejala14': 0
}

# UI Question fisikGenetik


class Question1(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)
        self.master = master  # Save reference to the master
        self.configure(fg_color="#FFFAF1")

        # Ganti dengan path gambar Anda
        img_hover1 = Image.open(img_path_hover1)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(
            relx=0.94, rely=0.005, anchor=customtkinter.CENTER)

        img_center = Image.open(img_path_center)
        self.img_center = CTkImage(img_center, size=(
            img_center.width, img_center.height))

        self.image_label_center = customtkinter.CTkLabel(
            self, image=self.img_center, text='')
        self.image_label_center.place(
            relx=0.5, rely=0.24, anchor=customtkinter.CENTER)

        self.button_prev = customtkinter.CTkButton(self, text='<', command=self.button_prev,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_prev.place(relx=0.1, rely=0.05,
                               anchor=customtkinter.CENTER)

        self.box_label = customtkinter.CTkFrame(
            self, width=285, height=62, fg_color="#F8DDDD", corner_radius=20)
        self.box_label.place(relx=0.5, rely=0.43, anchor=customtkinter.CENTER)

        self.label_quest = customtkinter.CTkLabel(self.box_label, text="Berapa Usia Anda?", fg_color='transparent', text_color='#C14856',
                                                  font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        # Option
        self.box = customtkinter.CTkFrame(
            self, width=375, height=334, fg_color="#C14856", corner_radius=33)
        self.box.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

        self.selected_option = None  # Store the selected option

        self.button_1 = customtkinter.CTkButton(self.box, text='< 20 tahun', command=self.button_1_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=51, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_1.place(relx=0.5, rely=0.15, anchor=customtkinter.CENTER)

        self.button_2 = customtkinter.CTkButton(self.box, text='20 sampai 65 tahun', command=self.button_2_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=51, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_2.place(relx=0.5, rely=0.35, anchor=customtkinter.CENTER)

        self.button_3 = customtkinter.CTkButton(self.box, text='> 65 tahun', command=self.button_3_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=51, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_3.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)

        self.button_next = customtkinter.CTkButton(self.box, text='>', command=self.button_next,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_next.place(relx=0.5, rely=0.77,
                               anchor=customtkinter.CENTER)

    def button_prev(self):
        self.master.switch_frame(Home)

    def button_next(self):
        if self.selected_option is not None:
            answers_fisikGenetikaGlukosa['question1'] = self.selected_option
            self.master.switch_frame(Question2)
            print(answers_fisikGenetikaGlukosa)

    def button_1_action(self):
        self.selected_option = 1
        self.update_button_colors()

    def button_2_action(self):
        self.selected_option = 2
        self.update_button_colors()

    def button_3_action(self):
        self.selected_option = 3
        self.update_button_colors()

    def update_button_colors(self):
        self.button_1.configure(
            fg_color="#FFFAF1" if self.selected_option != 1 else "#F8B5BB")
        self.button_2.configure(
            fg_color="#FFFAF1" if self.selected_option != 2 else "#F8B5BB")
        self.button_3.configure(
            fg_color="#FFFAF1" if self.selected_option != 3 else "#F8B5BB")


class Question2(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)
        self.master = master  # Save reference to the master
        self.configure(fg_color="#FFFAF1")

        # Ganti dengan path gambar Anda
        img_hover1 = Image.open(img_path_hover1)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(
            relx=0.94, rely=0.005, anchor=customtkinter.CENTER)

        img_center = Image.open(img_path_center)
        self.img_center = CTkImage(img_center, size=(
            img_center.width, img_center.height))

        self.image_label_center = customtkinter.CTkLabel(
            self, image=self.img_center, text='')
        self.image_label_center.place(
            relx=0.5, rely=0.24, anchor=customtkinter.CENTER)

        self.button_prev = customtkinter.CTkButton(self, text='<', command=self.button_prev,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_prev.place(relx=0.1, rely=0.05,
                               anchor=customtkinter.CENTER)

        self.box_label = customtkinter.CTkFrame(
            self, width=285, height=62, fg_color="#F8DDDD", corner_radius=20)
        self.box_label.place(relx=0.5, rely=0.43, anchor=customtkinter.CENTER)

        self.label_quest = customtkinter.CTkLabel(self.box_label, text="Jenis Kelamin Anda?", fg_color='transparent', text_color='#C14856',
                                                  font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        # Option
        self.box = customtkinter.CTkFrame(
            self, width=375, height=334, fg_color="#C14856", corner_radius=33)
        self.box.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

        self.selected_option = None  # Store the selected option

        self.button_1 = customtkinter.CTkButton(self.box, text='Laki-laki', command=self.button_1_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_1.place(relx=0.5, rely=0.20, anchor=CENTER)

        self.button_2 = customtkinter.CTkButton(self.box, text='Perempuan', command=self.button_2_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_2.place(relx=0.5, rely=0.45, anchor=CENTER)

        self.button_next = customtkinter.CTkButton(self.box, text='>', command=self.button_next,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_next.place(relx=0.5, rely=0.77,
                               anchor=customtkinter.CENTER)

    def button_prev(self):
        self.master.switch_frame(Question1)

    def button_next(self):
        if self.selected_option is not None:
            answers_fisikGenetikaGlukosa['question2'] = self.selected_option
            self.master.switch_frame(Question3)
            print(answers_fisikGenetikaGlukosa)

    def button_1_action(self):
        self.selected_option = 1
        self.update_button_colors()

    def button_2_action(self):
        self.selected_option = 0
        self.update_button_colors()

    def update_button_colors(self):
        self.button_1.configure(
            fg_color="#FFFAF1" if self.selected_option != 1 else "#F8B5BB")
        self.button_2.configure(
            fg_color="#FFFAF1" if self.selected_option != 0 else "#F8B5BB")


class Question3(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)
        self.master = master  # Save reference to the master
        self.configure(fg_color="#FFFAF1")

        # Image paths
        img_hover1 = Image.open(img_path_hover1)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        img_center = Image.open(img_path_center)
        self.img_center = CTkImage(img_center, size=(
            img_center.width, img_center.height))

        # Image labels
        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(
            relx=0.94, rely=0.005, anchor=customtkinter.CENTER)

        self.image_label_center = customtkinter.CTkLabel(
            self, image=self.img_center, text='')
        self.image_label_center.place(
            relx=0.5, rely=0.24, anchor=customtkinter.CENTER)

        # Previous button
        self.button_prev = customtkinter.CTkButton(self, text='<', command=self.button_prev,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51, width=65,
                                                   corner_radius=25, hover_color='#F8B5BB')
        self.button_prev.place(relx=0.1, rely=0.05,
                               anchor=customtkinter.CENTER)

        # Question label box
        self.box_label = customtkinter.CTkFrame(
            self, width=285, height=62, fg_color="#F8DDDD", corner_radius=20)
        self.box_label.place(relx=0.5, rely=0.43, anchor=customtkinter.CENTER)

        self.label_quest = customtkinter.CTkLabel(self.box_label, text="Tinggi Badan (cm) Anda?", fg_color='transparent', text_color='#C14856',
                                                  font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        # Options box
        self.box = customtkinter.CTkFrame(
            self, width=375, height=334, fg_color="#C14856", corner_radius=33)
        self.box.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

        # Slider box
        self.box_slider = customtkinter.CTkFrame(
            self.box, width=285, height=62, fg_color="#F8DDDD", corner_radius=20)
        self.box_slider.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.slider_value = IntVar()
        self.slider = customtkinter.CTkSlider(self.box_slider, from_=0, to=200, variable=self.slider_value,
                                              progress_color="#FFFAF1", button_color="#F8B5BB",
                                              button_hover_color="#F8B5BB", width=260, height=30,
                                              command=self.update_label)  # Adjust width here
        self.slider.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        # Slider value label
        self.box_label_slider = customtkinter.CTkFrame(
            self.box, width=70, height=62, fg_color="#FFFAF1", corner_radius=20)
        self.box_label_slider.place(
            relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        self.slider_value_label = customtkinter.CTkLabel(self.box_label_slider, text=str(self.slider_value.get()), text_color="#C14856",
                                                         font=customtkinter.CTkFont(family='Roboto', size=16, weight='bold'))
        self.slider_value_label.place(
            relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        # Next button
        self.button_next = customtkinter.CTkButton(self.box, text='>', command=self.button_next,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51, width=65,
                                                   corner_radius=25, hover_color='#F8B5BB')
        self.button_next.place(relx=0.5, rely=0.77,
                               anchor=customtkinter.CENTER)

    def button_prev(self):
        self.master.switch_frame(Question2)

    def button_next(self):
        if self.slider_value.get() != 0:
            answers_fisikGenetikaGlukosa['question3'] = self.slider_value.get()
            self.master.switch_frame(Question4)
            print(answers_fisikGenetikaGlukosa)

    def update_label(self, value):
        self.slider_value_label.configure(text=str(int(float(value))))


class Question4(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)
        self.master = master  # Save reference to the master
        self.configure(fg_color="#FFFAF1")

        # Image paths
        img_hover1 = Image.open(img_path_hover1)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        img_center = Image.open(img_path_center)
        self.img_center = CTkImage(img_center, size=(
            img_center.width, img_center.height))

        # Image labels
        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(
            relx=0.94, rely=0.005, anchor=customtkinter.CENTER)

        self.image_label_center = customtkinter.CTkLabel(
            self, image=self.img_center, text='')
        self.image_label_center.place(
            relx=0.5, rely=0.24, anchor=customtkinter.CENTER)

        # Previous button
        self.button_prev = customtkinter.CTkButton(self, text='<', command=self.button_prev,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51, width=65,
                                                   corner_radius=25, hover_color='#F8B5BB')
        self.button_prev.place(relx=0.1, rely=0.05,
                               anchor=customtkinter.CENTER)

        # Question label box
        self.box_label = customtkinter.CTkFrame(
            self, width=285, height=62, fg_color="#F8DDDD", corner_radius=20)
        self.box_label.place(relx=0.5, rely=0.43, anchor=customtkinter.CENTER)

        self.label_quest = customtkinter.CTkLabel(self.box_label, text="Berat Badan (kg) Anda?", fg_color='transparent', text_color='#C14856',
                                                  font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        # Options box
        self.box = customtkinter.CTkFrame(
            self, width=375, height=334, fg_color="#C14856", corner_radius=33)
        self.box.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

        # Slider box
        self.box_slider = customtkinter.CTkFrame(
            self.box, width=285, height=62, fg_color="#F8DDDD", corner_radius=20)
        self.box_slider.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.slider_value = IntVar()
        self.slider = customtkinter.CTkSlider(self.box_slider, from_=0, to=200, variable=self.slider_value,
                                              progress_color="#FFFAF1", button_color="#F8B5BB",
                                              button_hover_color="#F8B5BB", width=260, height=30,
                                              command=self.update_label)
        self.slider.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        # Slider value label
        self.box_label_slider = customtkinter.CTkFrame(
            self.box, width=70, height=62, fg_color="#FFFAF1", corner_radius=20)
        self.box_label_slider.place(
            relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        self.slider_value_label = customtkinter.CTkLabel(self.box_label_slider, text=str(self.slider_value.get()), text_color="#C14856",
                                                         font=customtkinter.CTkFont(family='Roboto', size=16, weight='bold'))
        self.slider_value_label.place(
            relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        # Next button
        self.button_next = customtkinter.CTkButton(self.box, text='>', command=self.button_next,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51, width=65,
                                                   corner_radius=25, hover_color='#F8B5BB')
        self.button_next.place(relx=0.5, rely=0.77,
                               anchor=customtkinter.CENTER)

    def button_prev(self):
        self.master.switch_frame(Question3)

    def button_next(self):
        if self.slider_value.get() != 0:
            answers_fisikGenetikaGlukosa['question4'] = float(
                self.slider_value.get())
            self.master.switch_frame(Question5)
            print(answers_fisikGenetikaGlukosa)

    def update_label(self, value):
        self.slider_value_label.configure(text=str(int(float(value))))


class Question5(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)
        self.master = master  # Save reference to the master
        self.configure(fg_color="#FFFAF1")

        # Image paths
        img_hover1 = Image.open(img_path_hover1)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        img_center = Image.open(img_path_center)
        self.img_center = CTkImage(img_center, size=(
            img_center.width, img_center.height))

        # Image labels
        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(
            relx=0.94, rely=0.005, anchor=customtkinter.CENTER)

        self.image_label_center = customtkinter.CTkLabel(
            self, image=self.img_center, text='')
        self.image_label_center.place(
            relx=0.5, rely=0.24, anchor=customtkinter.CENTER)

        # Previous button
        self.button_prev = customtkinter.CTkButton(self, text='<', command=self.button_prev,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51, width=65,
                                                   corner_radius=25, hover_color='#F8B5BB')
        self.button_prev.place(relx=0.1, rely=0.05,
                               anchor=customtkinter.CENTER)

        # Question label box
        self.box_label = customtkinter.CTkFrame(
            self, width=285, height=62, fg_color="#F8DDDD", corner_radius=20)
        self.box_label.place(relx=0.5, rely=0.43, anchor=customtkinter.CENTER)

        self.label_quest1 = customtkinter.CTkLabel(self.box_label, text="Apakah Anda tahu kadar ", fg_color='transparent', text_color='#C14856',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest1.place(relx=0.5, rely=0.27,
                                anchor=customtkinter.CENTER)
        self.label_quest2 = customtkinter.CTkLabel(self.box_label, text="gula darah Anda?", fg_color='transparent', text_color='#C14856',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest2.place(relx=0.5, rely=0.72,
                                anchor=customtkinter.CENTER)

        # Options box
        self.box = customtkinter.CTkFrame(
            self, width=375, height=334, fg_color="#C14856", corner_radius=33)
        self.box.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

        self.selected_option = None  # Store the selected option

        self.button_1 = customtkinter.CTkButton(self.box, text='Ya', command=self.button_1_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_1.place(relx=0.5, rely=0.20, anchor=CENTER)

        self.button_2 = customtkinter.CTkButton(self.box, text='Tidak', command=self.button_2_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_2.place(relx=0.5, rely=0.45, anchor=CENTER)

        # Next button
        self.button_next = customtkinter.CTkButton(self.box, text='>', command=self.button_next,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_next.place(relx=0.5, rely=0.77,
                               anchor=customtkinter.CENTER)

    def button_prev(self):
        self.master.switch_frame(Question4)

    def button_1_action(self):
        self.selected_option = 1
        # print("Selected option: Ya")
        self.update_button_colors()

    def button_2_action(self):
        self.selected_option = 0
        # print("Selected option: Tidak")
        self.update_button_colors()

    def button_next(self):
        if self.selected_option != None:
            answers_fisikGenetikaGlukosa['question5'] = self.selected_option
            if self.selected_option == 1:
                self.master.switch_frame(Question6)
            elif self.selected_option == 0:
                answers_fisikGenetikaGlukosa['question6'] = 0
                self.master.switch_frame(Question7)
            print(answers_fisikGenetikaGlukosa)

    def update_button_colors(self):
        self.button_1.configure(
            fg_color="#F8B5BB" if self.selected_option == 1 else "#FFFAF1")
        self.button_2.configure(
            fg_color="#F8B5BB" if self.selected_option == 0 else "#FFFAF1")


class Question6(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)
        self.master = master  # Save reference to the master
        self.configure(fg_color="#FFFAF1")

        # Image paths
        img_hover1 = Image.open(img_path_hover1)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        img_center = Image.open(img_path_center)
        self.img_center = CTkImage(img_center, size=(
            img_center.width, img_center.height))

        # Image labels
        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(
            relx=0.94, rely=0.005, anchor=customtkinter.CENTER)

        self.image_label_center = customtkinter.CTkLabel(
            self, image=self.img_center, text='')
        self.image_label_center.place(
            relx=0.5, rely=0.24, anchor=customtkinter.CENTER)

        # Previous button
        self.button_prev = customtkinter.CTkButton(self, text='<', command=self.button_prev,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_prev.place(relx=0.1, rely=0.05,
                               anchor=customtkinter.CENTER)

        # Question label box
        self.box_label = customtkinter.CTkFrame(
            self, width=285, height=62, fg_color="#F8DDDD", corner_radius=20)
        self.box_label.place(relx=0.5, rely=0.43, anchor=customtkinter.CENTER)

        self.label_quest1 = customtkinter.CTkLabel(self.box_label, text="Berapakah Kadar Gula ", fg_color='transparent', text_color='#C14856',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest1.place(relx=0.5, rely=0.27,
                                anchor=customtkinter.CENTER)
        self.label_quest2 = customtkinter.CTkLabel(self.box_label, text="Darah (mg/dL) Anda?", fg_color='transparent', text_color='#C14856',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest2.place(relx=0.5, rely=0.72,
                                anchor=customtkinter.CENTER)

        # Options box
        self.box = customtkinter.CTkFrame(
            self, width=375, height=334, fg_color="#C14856", corner_radius=33)
        self.box.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

        # Slider
        self.box_slider = customtkinter.CTkFrame(
            self.box, width=285, height=62, fg_color="#F8DDDD", corner_radius=20)
        self.box_slider.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.slider_value = customtkinter.IntVar()
        self.slider = customtkinter.CTkSlider(self.box_slider, from_=0, to=200, variable=self.slider_value,
                                              progress_color="#FFFAF1", button_color="#F8B5BB",
                                              button_hover_color="#F8B5BB", width=260, height=30, command=self.update_label)  # Adjust width here
        self.slider.place(relx=0.5, rely=0.5, anchor='center')

        # Label to display slider value
        self.box_label_slider = customtkinter.CTkFrame(
            self.box, width=70, height=62, fg_color="#FFFAF1", corner_radius=20)
        self.box_label_slider.place(
            relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        self.slider_value_label = customtkinter.CTkLabel(self.box_label_slider, text=str(self.slider_value.get()), text_color="#C14856",
                                                         font=customtkinter.CTkFont(family='Roboto', size=16, weight='bold'))
        self.slider_value_label.place(relx=0.5, rely=0.5, anchor='center')

        # Next button
        self.button_next = customtkinter.CTkButton(self.box, text='>', command=self.button_next,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_next.place(relx=0.5, rely=0.77,
                               anchor=customtkinter.CENTER)

    def button_prev(self):
        self.master.switch_frame(Question5)

    def button_next(self):
        if self.slider_value.get() != 0:
            answers_fisikGenetikaGlukosa['question6'] = self.slider_value.get()
            self.master.switch_frame(Question7)
            print(answers_fisikGenetikaGlukosa)

    def update_label(self, value):
        self.slider_value_label.configure(text=str(int(float(value))))


class Question7(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)
        self.master = master  # Save reference to the master
        self.configure(fg_color="#FFFAF1")

        # Image paths
        img_hover1 = Image.open(img_path_hover1)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        img_center = Image.open(img_path_center)
        self.img_center = CTkImage(img_center, size=(
            img_center.width, img_center.height))

        # Image labels
        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(
            relx=0.94, rely=0.005, anchor=customtkinter.CENTER)

        self.image_label_center = customtkinter.CTkLabel(
            self, image=self.img_center, text='')
        self.image_label_center.place(
            relx=0.5, rely=0.24, anchor=customtkinter.CENTER)

        self.button_prev = customtkinter.CTkButton(self, text='<', command=self.button_prev,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_prev.place(relx=0.1, rely=0.05, anchor=CENTER)

        self.box_label = customtkinter.CTkFrame(
            self, width=285, height=62, fg_color="#F8DDDD", corner_radius=20)
        self.box_label.place(relx=0.5, rely=0.43, anchor=CENTER)

        self.label_quest1 = customtkinter.CTkLabel(self.box_label, text="Adakah riwayat Diabetes ", fg_color='transparent', text_color='#C14856',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest1.place(relx=0.5, rely=0.27, anchor=CENTER)
        self.label_quest2 = customtkinter.CTkLabel(self.box_label, text="Keluarga Anda?", fg_color='transparent', text_color='#C14856',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest2.place(relx=0.5, rely=0.72, anchor=CENTER)

        # Option
        self.box = customtkinter.CTkFrame(
            self, width=375, height=334, fg_color="#C14856", corner_radius=33)
        self.box.place(relx=0.5, rely=0.8, anchor=CENTER)

        self.selected_option = None  # Store the selected option

        self.button_1 = customtkinter.CTkButton(self.box, text='Ya', command=self.button_1_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_1.place(relx=0.5, rely=0.20, anchor=CENTER)

        self.button_2 = customtkinter.CTkButton(self.box, text='Tidak', command=self.button_2_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_2.place(relx=0.5, rely=0.45, anchor=CENTER)

        self.button_next = customtkinter.CTkButton(self.box, text='>', command=self.button_next,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_next.place(relx=0.5, rely=0.77, anchor=CENTER)

    # Load gambar

    def button_prev(self):
        if answers_fisikGenetikaGlukosa['question5'] == 0:
            self.master.switch_frame(Question5)
        else:
            self.master.switch_frame(Question6)

    def button_next(self):
        if self.selected_option != None:
            answers_fisikGenetikaGlukosa['question7'] = self.selected_option
            self.master.switch_frame(Gejala1)
            print(answers_fisikGenetikaGlukosa)

    def button_1_action(self):
        self.selected_option = 1
        self.update_button_colors()
        # print("Anda memilih ya.")

    def button_2_action(self):
        self.selected_option = 0
        self.update_button_colors()
        # print("Anda memilih ya.")

    def update_button_colors(self):
        self.button_1.configure(
            fg_color="#FFFAF1" if self.selected_option != 1 else "#F8B5BB")
        self.button_2.configure(
            fg_color="#FFFAF1" if self.selected_option != 0 else "#F8B5BB")

# check risk fisikGenetik

def check_riskQuetion():
    # Load your rules CSV
    path_rulesUmum = os.path.join(root_directory,"Rule","rulesUmum.csv")
    rules_df = pd.read_csv(path_rulesUmum)

    # Once all questions are answered and stored in answers_fisikGenetikaGlukosa, you can use the check_risk function like this:
    usia = answers_fisikGenetikaGlukosa.get('question1')
    kelamin = answers_fisikGenetikaGlukosa.get('question2')
    height_in_meters = answers_fisikGenetikaGlukosa.get('question3')/100
    weight_in_kg = answers_fisikGenetikaGlukosa.get('question4')
    riwayat = answers_fisikGenetikaGlukosa.get('question7')
    
    bmi = weight_in_kg/(height_in_meters**2)
    
    if bmi < 25:
        bmi = 0
    elif bmi >= 25:
        bmi = 1
    
    for index, row in rules_df.iterrows():
        usia_rule = row['umur']
        kelamin_rule = row['jenis_kelamin']
        bmi_rule = row['bmi']
        riwayat_rule = row['riwayat']

        # Check usia
        if usia != usia_rule:
            continue

        # Check kelamin
        if kelamin != kelamin_rule:
            continue

        # Check BMI
        if bmi != bmi_rule:
            continue

        # Check riwayat
        if riwayat != riwayat_rule:
            continue
        
        # Jika semua aturan cocok
        return row['risiko']
    
    return 0

# UI Question gejalaAktivitas


class Gejala1(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)
        self.master = master  # Save reference to the master
        self.configure(fg_color="#FFFAF1")

        # Title box
        self.box_title = customtkinter.CTkFrame(
            self, width=140, height=42, fg_color="#EC9B9B", corner_radius=13)
        self.box_title.place(relx=0.22, rely=0.07, anchor='center')

        self.label_title = customtkinter.CTkLabel(self.box_title, text="Prediksi Gejala", fg_color='transparent', text_color='#FFFFFF',
                                                  font=customtkinter.CTkFont(family='Roboto', size=15, weight='bold'))
        self.label_title.place(relx=0.5, rely=0.5, anchor='center')

        # Image initialization
        img_hover1 = Image.open(img_path_hover1)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(relx=0.94, rely=0.005, anchor='center')

        # Option box
        self.box_options = customtkinter.CTkFrame(
            self, width=350, height=520, fg_color="#F8DDDD", corner_radius=33)
        self.box_options.place(relx=0.5, rely=0.59, anchor='center')

        # Image center
        img_center = Image.open(img_path_center2)
        self.img_center = CTkImage(img_center, size=(
            img_center.width, img_center.height))

        self.image_label_center = customtkinter.CTkLabel(
            self.box_options, image=self.img_center, text='')
        self.image_label_center.place(relx=0.5, rely=0.18, anchor='center')

        # Previous button
        self.button_prev = customtkinter.CTkButton(self.box_options, text='<', command=self.button_prev,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_prev.place(relx=0.13, rely=0.93, anchor='center')

        # Question box
        self.box_question = customtkinter.CTkFrame(
            self.box_options, width=304, height=80, fg_color="#EC9B9B", corner_radius=20)
        self.box_question.place(relx=0.5, rely=0.37, anchor='center')

        self.label_quest1 = customtkinter.CTkLabel(self.box_question, text="Apakah Anda sering ", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest1.place(relx=0.5, rely=0.32, anchor='center')
        self.label_quest2 = customtkinter.CTkLabel(self.box_question, text="merasa haus?", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest2.place(relx=0.5, rely=0.67, anchor='center')

        self.selected_option = None  # Store the selected option

        # Buttons
        self.button_1 = customtkinter.CTkButton(self.box_options, text='Ya', command=self.button_1_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_1.place(relx=0.5, rely=0.55, anchor='center')

        self.button_2 = customtkinter.CTkButton(self.box_options, text='Tidak', command=self.button_2_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_2.place(relx=0.5, rely=0.70, anchor='center')

        # Next button
        self.button_next = customtkinter.CTkButton(self.box_options, text='>', command=self.button_next,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_next.place(relx=0.87, rely=0.93, anchor='center')

    # Load gambar

    def button_prev(self):
        self.master.switch_frame(Question7)

    def button_next(self):
        if self.selected_option != None:
            answers_gejala['gejala1'] = self.selected_option
            self.master.switch_frame(Gejala2)
            print(answers_gejala)

    def button_1_action(self):
        self.selected_option = 1
        self.update_button_colors()
        # print("Anda memilih ya.")

    def button_2_action(self):
        self.selected_option = 0
        self.update_button_colors()
        # print("Anda memilih ya.")

    def update_button_colors(self):
        self.button_1.configure(
            fg_color="#FFFAF1" if self.selected_option != 1 else "#F8B5BB")
        self.button_2.configure(
            fg_color="#FFFAF1" if self.selected_option != 0 else "#F8B5BB")


class Gejala2(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)
        self.master = master  # Save reference to the master
        self.configure(fg_color="#FFFAF1")

        # Title box
        self.box_title = customtkinter.CTkFrame(
            self, width=140, height=42, fg_color="#EC9B9B", corner_radius=13)
        self.box_title.place(relx=0.22, rely=0.07, anchor='center')

        self.label_title = customtkinter.CTkLabel(self.box_title, text="Prediksi Gejala", fg_color='transparent', text_color='#FFFFFF',
                                                  font=customtkinter.CTkFont(family='Roboto', size=15, weight='bold'))
        self.label_title.place(relx=0.5, rely=0.5, anchor='center')

        # Image initialization
        img_hover1 = Image.open(img_path_hover1)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(relx=0.94, rely=0.005, anchor='center')

        # Option box
        self.box_options = customtkinter.CTkFrame(
            self, width=350, height=520, fg_color="#F8DDDD", corner_radius=33)
        self.box_options.place(relx=0.5, rely=0.59, anchor='center')

        # Image center
        img_center = Image.open(img_path_center3)
        self.img_center = CTkImage(img_center, size=(
            img_center.width, img_center.height))

        self.image_label_center = customtkinter.CTkLabel(
            self.box_options, image=self.img_center, text='')
        self.image_label_center.place(relx=0.5, rely=0.18, anchor='center')

        # Previous button
        self.button_prev = customtkinter.CTkButton(self.box_options, text='<', command=self.button_prev,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_prev.place(relx=0.13, rely=0.93, anchor='center')

        # Question box
        self.box_question = customtkinter.CTkFrame(
            self.box_options, width=304, height=80, fg_color="#EC9B9B", corner_radius=20)
        self.box_question.place(relx=0.5, rely=0.37, anchor='center')

        self.label_quest1 = customtkinter.CTkLabel(self.box_question, text="Apakah Anda sering merasa", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest1.place(relx=0.5, rely=0.20, anchor='center')
        self.label_quest2 = customtkinter.CTkLabel(self.box_question, text="lapar berlebih meskipun ", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest2.place(relx=0.5, rely=0.505, anchor='center')
        self.label_quest3 = customtkinter.CTkLabel(self.box_question, text="sudah makan ?", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest3.place(relx=0.5, rely=0.8, anchor='center')
        self.selected_option = None  # Store the selected option

        # Buttons
        self.button_1 = customtkinter.CTkButton(self.box_options, text='Ya', command=self.button_1_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_1.place(relx=0.5, rely=0.55, anchor='center')

        self.button_2 = customtkinter.CTkButton(self.box_options, text='Tidak', command=self.button_2_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_2.place(relx=0.5, rely=0.70, anchor='center')

        # Next button
        self.button_next = customtkinter.CTkButton(self.box_options, text='>', command=self.button_next,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_next.place(relx=0.87, rely=0.93, anchor='center')

    # Load gambar

    def button_prev(self):
        self.master.switch_frame(Gejala1)

    def button_next(self):
        if self.selected_option != None:
            answers_gejala['gejala2'] = self.selected_option
            self.master.switch_frame(Gejala3)
            print(answers_gejala)

    def button_1_action(self):
        self.selected_option = 1
        self.update_button_colors()
        # print("Anda memilih ya.")

    def button_2_action(self):
        self.selected_option = 0
        self.update_button_colors()
        # print("Anda memilih ya.")

    def update_button_colors(self):
        self.button_1.configure(
            fg_color="#FFFAF1" if self.selected_option != 1 else "#F8B5BB")
        self.button_2.configure(
            fg_color="#FFFAF1" if self.selected_option != 0 else "#F8B5BB")


class Gejala3(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)
        self.master = master  # Save reference to the master
        self.configure(fg_color="#FFFAF1")

        # Title box
        self.box_title = customtkinter.CTkFrame(
            self, width=140, height=42, fg_color="#EC9B9B", corner_radius=13)
        self.box_title.place(relx=0.22, rely=0.07, anchor='center')

        self.label_title = customtkinter.CTkLabel(self.box_title, text="Prediksi Gejala", fg_color='transparent', text_color='#FFFFFF',
                                                  font=customtkinter.CTkFont(family='Roboto', size=15, weight='bold'))
        self.label_title.place(relx=0.5, rely=0.5, anchor='center')

        # Image initialization
        img_hover1 = Image.open(img_path_hover1)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(relx=0.94, rely=0.005, anchor='center')

        # Option box
        self.box_options = customtkinter.CTkFrame(
            self, width=350, height=520, fg_color="#F8DDDD", corner_radius=33)
        self.box_options.place(relx=0.5, rely=0.59, anchor='center')

        # Image center

        img_center = Image.open(img_path_center4)
        self.img_center = CTkImage(img_center, size=(
            img_center.width, img_center.height))

        self.image_label_center = customtkinter.CTkLabel(
            self.box_options, image=self.img_center, text='')
        self.image_label_center.place(relx=0.5, rely=0.15, anchor='center')

        # Previous button
        self.button_prev = customtkinter.CTkButton(self.box_options, text='<', command=self.button_prev,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_prev.place(relx=0.13, rely=0.93, anchor='center')

        # Question box
        self.box_question = customtkinter.CTkFrame(
            self.box_options, width=304, height=80, fg_color="#EC9B9B", corner_radius=20)
        self.box_question.place(relx=0.5, rely=0.37, anchor='center')

        self.label_quest1 = customtkinter.CTkLabel(self.box_question, text="Apakah Anda Sering ", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest1.place(relx=0.5, rely=0.20, anchor='center')
        self.label_quest2 = customtkinter.CTkLabel(self.box_question, text="mengonsumsi Makanan ", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest2.place(relx=0.5, rely=0.505, anchor='center')
        self.label_quest3 = customtkinter.CTkLabel(self.box_question, text="Tinggi Gula dan Lemak ?", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest3.place(relx=0.5, rely=0.8, anchor='center')

        self.selected_option = None  # Store the selected option

        # Buttons
        self.button_1 = customtkinter.CTkButton(self.box_options, text='Ya', command=self.button_1_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_1.place(relx=0.5, rely=0.55, anchor='center')

        self.button_2 = customtkinter.CTkButton(self.box_options, text='Tidak', command=self.button_2_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_2.place(relx=0.5, rely=0.70, anchor='center')

        # Next button
        self.button_next = customtkinter.CTkButton(self.box_options, text='>', command=self.button_next,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_next.place(relx=0.87, rely=0.93, anchor='center')

    # Load gambar

    def button_prev(self):
        self.master.switch_frame(Gejala2)

    def button_next(self):
        if self.selected_option != None:
            answers_gejala['gejala3'] = self.selected_option
            self.master.switch_frame(Gejala4)
            print(answers_gejala)

    def button_1_action(self):
        self.selected_option = 1
        self.update_button_colors()
        # print("Anda memilih ya.")

    def button_2_action(self):
        self.selected_option = 0
        self.update_button_colors()
        # print("Anda memilih ya.")

    def update_button_colors(self):
        self.button_1.configure(
            fg_color="#FFFAF1" if self.selected_option != 1 else "#F8B5BB")
        self.button_2.configure(
            fg_color="#FFFAF1" if self.selected_option != 0 else "#F8B5BB")


class Gejala4(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)
        self.master = master  # Save reference to the master
        self.configure(fg_color="#FFFAF1")

        # Title box
        self.box_title = customtkinter.CTkFrame(
            self, width=140, height=42, fg_color="#EC9B9B", corner_radius=13)
        self.box_title.place(relx=0.22, rely=0.07, anchor='center')

        self.label_title = customtkinter.CTkLabel(self.box_title, text="Prediksi Gejala", fg_color='transparent', text_color='#FFFFFF',
                                                  font=customtkinter.CTkFont(family='Roboto', size=15, weight='bold'))
        self.label_title.place(relx=0.5, rely=0.5, anchor='center')

        # Image initialization
        img_hover1 = Image.open(img_path_hover1)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(relx=0.94, rely=0.005, anchor='center')

        # Option box
        self.box_options = customtkinter.CTkFrame(
            self, width=350, height=520, fg_color="#F8DDDD", corner_radius=33)
        self.box_options.place(relx=0.5, rely=0.59, anchor='center')

        # Image center

        img_center = Image.open(img_path_center5)
        self.img_center = CTkImage(img_center, size=(
            img_center.width, img_center.height))

        self.image_label_center = customtkinter.CTkLabel(
            self.box_options, image=self.img_center, text='')
        self.image_label_center.place(relx=0.5, rely=0.18, anchor='center')

        # Previous button
        self.button_prev = customtkinter.CTkButton(self.box_options, text='<', command=self.button_prev,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_prev.place(relx=0.13, rely=0.93, anchor='center')

        # Question box
        self.box_question = customtkinter.CTkFrame(
            self.box_options, width=304, height=80, fg_color="#EC9B9B", corner_radius=20)
        self.box_question.place(relx=0.5, rely=0.37, anchor='center')

        self.label_quest1 = customtkinter.CTkLabel(self.box_question, text="Apakah Anda sering buang air ", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest1.place(relx=0.5, rely=0.32, anchor='center')
        self.label_quest2 = customtkinter.CTkLabel(self.box_question, text="kecil, terutama di malam hari?", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest2.place(relx=0.5, rely=0.67, anchor='center')
        self.selected_option = None  # Store the selected option

        # Buttons
        self.button_1 = customtkinter.CTkButton(self.box_options, text='Ya', command=self.button_1_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_1.place(relx=0.5, rely=0.55, anchor='center')

        self.button_2 = customtkinter.CTkButton(self.box_options, text='Tidak', command=self.button_2_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_2.place(relx=0.5, rely=0.70, anchor='center')

        # Next button
        self.button_next = customtkinter.CTkButton(self.box_options, text='>', command=self.button_next,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_next.place(relx=0.87, rely=0.93, anchor='center')

    # Load gambar

    def button_prev(self):
        self.master.switch_frame(Gejala3)

    def button_next(self):
        if self.selected_option != None:
            answers_gejala['gejala4'] = self.selected_option
            self.master.switch_frame(Gejala5)
            print(answers_gejala)

    def button_1_action(self):
        self.selected_option = 1
        self.update_button_colors()
        # print("Anda memilih ya.")

    def button_2_action(self):
        self.selected_option = 0
        self.update_button_colors()
        # print("Anda memilih ya.")

    def update_button_colors(self):
        self.button_1.configure(
            fg_color="#FFFAF1" if self.selected_option != 1 else "#F8B5BB")
        self.button_2.configure(
            fg_color="#FFFAF1" if self.selected_option != 0 else "#F8B5BB")


class Gejala5(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)
        self.master = master  # Save reference to the master
        self.configure(fg_color="#FFFAF1")

        # Title box
        self.box_title = customtkinter.CTkFrame(
            self, width=140, height=42, fg_color="#EC9B9B", corner_radius=13)
        self.box_title.place(relx=0.22, rely=0.07, anchor='center')

        self.label_title = customtkinter.CTkLabel(self.box_title, text="Prediksi Gejala", fg_color='transparent', text_color='#FFFFFF',
                                                  font=customtkinter.CTkFont(family='Roboto', size=15, weight='bold'))
        self.label_title.place(relx=0.5, rely=0.5, anchor='center')

        # Image initialization
        img_hover1 = Image.open(img_path_hover1)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(relx=0.94, rely=0.005, anchor='center')

        # Option box
        self.box_options = customtkinter.CTkFrame(
            self, width=350, height=520, fg_color="#F8DDDD", corner_radius=33)
        self.box_options.place(relx=0.5, rely=0.59, anchor='center')

        # Image center

        img_center = Image.open(img_path_center6)
        self.img_center = CTkImage(img_center, size=(
            img_center.width, img_center.height))

        self.image_label_center = customtkinter.CTkLabel(
            self.box_options, image=self.img_center, text='')
        self.image_label_center.place(relx=0.5, rely=0.18, anchor='center')

        # Previous button
        self.button_prev = customtkinter.CTkButton(self.box_options, text='<', command=self.button_prev,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_prev.place(relx=0.13, rely=0.93, anchor='center')

        # Question box
        self.box_question = customtkinter.CTkFrame(
            self.box_options, width=304, height=80, fg_color="#EC9B9B", corner_radius=20)
        self.box_question.place(relx=0.5, rely=0.37, anchor='center')

        self.label_quest1 = customtkinter.CTkLabel(self.box_question, text="Apakah Anda merasa ", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest1.place(relx=0.5, rely=0.20, anchor='center')
        self.label_quest2 = customtkinter.CTkLabel(self.box_question, text="lelah atau lemah tanpa ", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest2.place(relx=0.5, rely=0.505, anchor='center')
        self.label_quest3 = customtkinter.CTkLabel(self.box_question, text="sebab yang jelas?", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest3.place(relx=0.5, rely=0.8, anchor='center')
        self.selected_option = None  # Store the selected option

        # Buttons
        self.button_1 = customtkinter.CTkButton(self.box_options, text='Ya', command=self.button_1_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_1.place(relx=0.5, rely=0.55, anchor='center')

        self.button_2 = customtkinter.CTkButton(self.box_options, text='Tidak', command=self.button_2_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_2.place(relx=0.5, rely=0.70, anchor='center')

        # Next button
        self.button_next = customtkinter.CTkButton(self.box_options, text='>', command=self.button_next,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_next.place(relx=0.87, rely=0.93, anchor='center')

    # Load gambar

    def button_prev(self):
        self.master.switch_frame(Gejala4)

    def button_next(self):
        if self.selected_option != None:
            answers_gejala['gejala5'] = self.selected_option
            self.master.switch_frame(Gejala6)
            print(answers_gejala)

    def button_1_action(self):
        self.selected_option = 1
        self.update_button_colors()
        # print("Anda memilih ya.")

    def button_2_action(self):
        self.selected_option = 0
        self.update_button_colors()
        # print("Anda memilih ya.")

    def update_button_colors(self):
        self.button_1.configure(
            fg_color="#FFFAF1" if self.selected_option != 1 else "#F8B5BB")
        self.button_2.configure(
            fg_color="#FFFAF1" if self.selected_option != 0 else "#F8B5BB")


class Gejala6(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)
        self.master = master  # Save reference to the master
        self.configure(fg_color="#FFFAF1")

        # Title box
        self.box_title = customtkinter.CTkFrame(
            self, width=140, height=42, fg_color="#EC9B9B", corner_radius=13)
        self.box_title.place(relx=0.22, rely=0.07, anchor='center')

        self.label_title = customtkinter.CTkLabel(self.box_title, text="Prediksi Gejala", fg_color='transparent', text_color='#FFFFFF',
                                                  font=customtkinter.CTkFont(family='Roboto', size=15, weight='bold'))
        self.label_title.place(relx=0.5, rely=0.5, anchor='center')

        # Image initialization
        img_hover1 = Image.open(img_path_hover1)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(relx=0.94, rely=0.005, anchor='center')

        # Option box
        self.box_options = customtkinter.CTkFrame(
            self, width=350, height=520, fg_color="#F8DDDD", corner_radius=33)
        self.box_options.place(relx=0.5, rely=0.59, anchor='center')

        # Image center

        img_center = Image.open(img_path_center7)
        self.img_center = CTkImage(img_center, size=(
            img_center.width, img_center.height))

        self.image_label_center = customtkinter.CTkLabel(
            self.box_options, image=self.img_center, text='')
        self.image_label_center.place(relx=0.5, rely=0.18, anchor='center')

        # Previous button
        self.button_prev = customtkinter.CTkButton(self.box_options, text='<', command=self.button_prev,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_prev.place(relx=0.13, rely=0.93, anchor='center')

        # Question box
        self.box_question = customtkinter.CTkFrame(
            self.box_options, width=304, height=80, fg_color="#EC9B9B", corner_radius=20)
        self.box_question.place(relx=0.5, rely=0.37, anchor='center')

        self.label_quest1 = customtkinter.CTkLabel(self.box_question, text="Apakah Anda mengalami ", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest1.place(relx=0.5, rely=0.32, anchor='center')
        self.label_quest2 = customtkinter.CTkLabel(self.box_question, text="penglihatan kabur ?", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest2.place(relx=0.5, rely=0.67, anchor='center')

        self.selected_option = None  # Store the selected option

        # Buttons
        self.button_1 = customtkinter.CTkButton(self.box_options, text='Ya', command=self.button_1_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_1.place(relx=0.5, rely=0.55, anchor='center')

        self.button_2 = customtkinter.CTkButton(self.box_options, text='Tidak', command=self.button_2_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_2.place(relx=0.5, rely=0.70, anchor='center')

        # Next button
        self.button_next = customtkinter.CTkButton(self.box_options, text='>', command=self.button_next,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_next.place(relx=0.87, rely=0.93, anchor='center')

    # Load gambar

    def button_prev(self):
        self.master.switch_frame(Gejala5)

    def button_next(self):
        if self.selected_option != None:
            answers_gejala['gejala6'] = self.selected_option
            self.master.switch_frame(Gejala7)
            print(answers_gejala)

    def button_1_action(self):
        self.selected_option = 1
        self.update_button_colors()
        # print("Anda memilih ya.")

    def button_2_action(self):
        self.selected_option = 0
        self.update_button_colors()
        # print("Anda memilih ya.")

    def update_button_colors(self):
        self.button_1.configure(
            fg_color="#FFFAF1" if self.selected_option != 1 else "#F8B5BB")
        self.button_2.configure(
            fg_color="#FFFAF1" if self.selected_option != 0 else "#F8B5BB")


class Gejala7(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)
        self.master = master  # Save reference to the master
        self.configure(fg_color="#FFFAF1")

        # Title box
        self.box_title = customtkinter.CTkFrame(
            self, width=140, height=42, fg_color="#EC9B9B", corner_radius=13)
        self.box_title.place(relx=0.22, rely=0.07, anchor='center')

        self.label_title = customtkinter.CTkLabel(self.box_title, text="Prediksi Gejala", fg_color='transparent', text_color='#FFFFFF',
                                                  font=customtkinter.CTkFont(family='Roboto', size=15, weight='bold'))
        self.label_title.place(relx=0.5, rely=0.5, anchor='center')

        # Image initialization
        img_hover1 = Image.open(img_path_hover1)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(relx=0.94, rely=0.005, anchor='center')

        # Option box
        self.box_options = customtkinter.CTkFrame(
            self, width=350, height=520, fg_color="#F8DDDD", corner_radius=33)
        self.box_options.place(relx=0.5, rely=0.59, anchor='center')

        # Image center
        
        img_center = Image.open(img_path_center8)
        self.img_center = CTkImage(img_center, size=(
            img_center.width, img_center.height))

        self.image_label_center = customtkinter.CTkLabel(
            self.box_options, image=self.img_center, text='')
        self.image_label_center.place(relx=0.5, rely=0.18, anchor='center')

        # Previous button
        self.button_prev = customtkinter.CTkButton(self.box_options, text='<', command=self.button_prev,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_prev.place(relx=0.13, rely=0.93, anchor='center')

        # Question box
        self.box_question = customtkinter.CTkFrame(
            self.box_options, width=304, height=80, fg_color="#EC9B9B", corner_radius=20)
        self.box_question.place(relx=0.5, rely=0.37, anchor='center')

        self.label_quest1 = customtkinter.CTkLabel(self.box_question, text="Apakah Anda sering ", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest1.place(relx=0.5, rely=0.32, anchor='center')
        self.label_quest2 = customtkinter.CTkLabel(self.box_question, text="mengalami stress?", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest2.place(relx=0.5, rely=0.67, anchor='center')

        self.selected_option = None  # Store the selected option

        # Buttons
        self.button_1 = customtkinter.CTkButton(self.box_options, text='Ya', command=self.button_1_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_1.place(relx=0.5, rely=0.55, anchor='center')

        self.button_2 = customtkinter.CTkButton(self.box_options, text='Tidak', command=self.button_2_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_2.place(relx=0.5, rely=0.70, anchor='center')

        # Next button
        self.button_next = customtkinter.CTkButton(self.box_options, text='>', command=self.button_next,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_next.place(relx=0.87, rely=0.93, anchor='center')

    # Load gambar

    def button_prev(self):
        self.master.switch_frame(Question6)

    def button_next(self):
        if self.selected_option != None:
            answers_gejala['gejala7'] = self.selected_option
            self.master.switch_frame(Gejala8)
            print(answers_gejala)

    def button_1_action(self):
        self.selected_option = 1
        self.update_button_colors()
        # print("Anda memilih ya.")

    def button_2_action(self):
        self.selected_option = 0
        self.update_button_colors()
        # print("Anda memilih ya.")

    def update_button_colors(self):
        self.button_1.configure(
            fg_color="#FFFAF1" if self.selected_option != 1 else "#F8B5BB")
        self.button_2.configure(
            fg_color="#FFFAF1" if self.selected_option != 0 else "#F8B5BB")


class Gejala8(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)
        self.master = master  # Save reference to the master
        self.configure(fg_color="#FFFAF1")

        # Title box
        self.box_title = customtkinter.CTkFrame(
            self, width=140, height=42, fg_color="#EC9B9B", corner_radius=13)
        self.box_title.place(relx=0.22, rely=0.07, anchor='center')

        self.label_title = customtkinter.CTkLabel(self.box_title, text="Prediksi Gejala", fg_color='transparent', text_color='#FFFFFF',
                                                  font=customtkinter.CTkFont(family='Roboto', size=15, weight='bold'))
        self.label_title.place(relx=0.5, rely=0.5, anchor='center')

        # Image initialization
        img_hover1 = Image.open(img_path_hover1)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(relx=0.94, rely=0.005, anchor='center')

        # Option box
        self.box_options = customtkinter.CTkFrame(
            self, width=350, height=520, fg_color="#F8DDDD", corner_radius=33)
        self.box_options.place(relx=0.5, rely=0.59, anchor='center')

        # Image center
        img_center = Image.open(img_path_center9)
        self.img_center = CTkImage(img_center, size=(
            img_center.width, img_center.height))

        self.image_label_center = customtkinter.CTkLabel(
            self.box_options, image=self.img_center, text='')
        self.image_label_center.place(relx=0.5, rely=0.18, anchor='center')

        # Previous button
        self.button_prev = customtkinter.CTkButton(self.box_options, text='<', command=self.button_prev,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_prev.place(relx=0.13, rely=0.93, anchor='center')

        # Question box
        self.box_question = customtkinter.CTkFrame(
            self.box_options, width=304, height=80, fg_color="#EC9B9B", corner_radius=20)
        self.box_question.place(relx=0.5, rely=0.37, anchor='center')

        self.label_quest1 = customtkinter.CTkLabel(self.box_question, text="Apakah Anda sering merasa ", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest1.place(relx=0.5, rely=0.20, anchor='center')
        self.label_quest2 = customtkinter.CTkLabel(self.box_question, text="kesemutan atau mati rasa ", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest2.place(relx=0.5, rely=0.505, anchor='center')
        self.label_quest3 = customtkinter.CTkLabel(self.box_question, text="ditangan atau kaki?", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest3.place(relx=0.5, rely=0.8, anchor='center')
        self.selected_option = None  # Store the selected option

        # Buttons
        self.button_1 = customtkinter.CTkButton(self.box_options, text='Ya', command=self.button_1_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_1.place(relx=0.5, rely=0.55, anchor='center')

        self.button_2 = customtkinter.CTkButton(self.box_options, text='Tidak', command=self.button_2_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_2.place(relx=0.5, rely=0.70, anchor='center')

        # Next button
        self.button_next = customtkinter.CTkButton(self.box_options, text='>', command=self.button_next,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_next.place(relx=0.87, rely=0.93, anchor='center')

    # Load gambar

    def button_prev(self):
        self.master.switch_frame(Gejala7)

    def button_next(self):
        if self.selected_option != None:
            answers_gejala['gejala8'] = self.selected_option
            self.master.switch_frame(Gejala9)
            print(answers_gejala)

    def button_1_action(self):
        self.selected_option = 1
        self.update_button_colors()
        # print("Anda memilih ya.")

    def button_2_action(self):
        self.selected_option = 0
        self.update_button_colors()
        # print("Anda memilih ya.")

    def update_button_colors(self):
        self.button_1.configure(
            fg_color="#FFFAF1" if self.selected_option != 1 else "#F8B5BB")
        self.button_2.configure(
            fg_color="#FFFAF1" if self.selected_option != 0 else "#F8B5BB")


class Gejala9(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)
        self.master = master  # Save reference to the master
        self.configure(fg_color="#FFFAF1")

        # Title box
        self.box_title = customtkinter.CTkFrame(
            self, width=140, height=42, fg_color="#EC9B9B", corner_radius=13)
        self.box_title.place(relx=0.22, rely=0.07, anchor='center')

        self.label_title = customtkinter.CTkLabel(self.box_title, text="Prediksi Gejala", fg_color='transparent', text_color='#FFFFFF',
                                                  font=customtkinter.CTkFont(family='Roboto', size=15, weight='bold'))
        self.label_title.place(relx=0.5, rely=0.5, anchor='center')

        # Image initialization
        img_hover1 = Image.open(img_path_hover1)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(relx=0.94, rely=0.005, anchor='center')

        # Option box
        self.box_options = customtkinter.CTkFrame(
            self, width=350, height=520, fg_color="#F8DDDD", corner_radius=33)
        self.box_options.place(relx=0.5, rely=0.59, anchor='center')

        # Image center
        
        img_center = Image.open(img_path_center10)
        self.img_center = CTkImage(img_center, size=(
            img_center.width, img_center.height))

        self.image_label_center = customtkinter.CTkLabel(
            self.box_options, image=self.img_center, text='')
        self.image_label_center.place(relx=0.5, rely=0.18, anchor='center')

        # Previous button
        self.button_prev = customtkinter.CTkButton(self.box_options, text='<', command=self.button_prev,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_prev.place(relx=0.13, rely=0.93, anchor='center')

        # Question box
        self.box_question = customtkinter.CTkFrame(
            self.box_options, width=310, height=95, fg_color="#EC9B9B", corner_radius=20)
        self.box_question.place(relx=0.5, rely=0.37, anchor='center')

        self.label_quest1 = customtkinter.CTkLabel(self.box_question, text="Apakah Anda sering mengalami ", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest1.place(relx=0.5, rely=0.22, anchor='center')
        self.label_quest2 = customtkinter.CTkLabel(self.box_question, text="infeksi kulit, gusi, atau ", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest2.place(relx=0.5, rely=0.48, anchor='center')
        self.label_quest3 = customtkinter.CTkLabel(self.box_question, text="luka yang lambat sembuh?", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest3.place(relx=0.5, rely=0.76, anchor='center')
        self.selected_option = None  # Store the selected option

        # Buttons
        self.button_1 = customtkinter.CTkButton(self.box_options, text='Ya', command=self.button_1_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_1.place(relx=0.5, rely=0.55, anchor='center')

        self.button_2 = customtkinter.CTkButton(self.box_options, text='Tidak', command=self.button_2_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_2.place(relx=0.5, rely=0.70, anchor='center')

        # Next button
        self.button_next = customtkinter.CTkButton(self.box_options, text='>', command=self.button_next,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_next.place(relx=0.87, rely=0.93, anchor='center')

    # Load gambar

    def button_prev(self):
        self.master.switch_frame(Gejala8)

    def button_next(self):
        if self.selected_option != None:
            answers_gejala['gejala9'] = self.selected_option
            self.master.switch_frame(Gejala10)
            print(answers_gejala)

    def button_1_action(self):
        self.selected_option = 1
        self.update_button_colors()
        # print("Anda memilih ya.")

    def button_2_action(self):
        self.selected_option = 0
        self.update_button_colors()
        # print("Anda memilih ya.")

    def update_button_colors(self):
        self.button_1.configure(
            fg_color="#FFFAF1" if self.selected_option != 1 else "#F8B5BB")
        self.button_2.configure(
            fg_color="#FFFAF1" if self.selected_option != 0 else "#F8B5BB")


class Gejala10(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)
        self.master = master  # Save reference to the master
        self.configure(fg_color="#FFFAF1")

        # Title box
        self.box_title = customtkinter.CTkFrame(
            self, width=140, height=42, fg_color="#EC9B9B", corner_radius=13)
        self.box_title.place(relx=0.22, rely=0.07, anchor='center')

        self.label_title = customtkinter.CTkLabel(self.box_title, text="Prediksi Gejala", fg_color='transparent', text_color='#FFFFFF',
                                                  font=customtkinter.CTkFont(family='Roboto', size=15, weight='bold'))
        self.label_title.place(relx=0.5, rely=0.5, anchor='center')

        # Image initialization
        img_hover1 = Image.open(img_path_hover1)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(relx=0.94, rely=0.005, anchor='center')

        # Option box
        self.box_options = customtkinter.CTkFrame(
            self, width=350, height=520, fg_color="#F8DDDD", corner_radius=33)
        self.box_options.place(relx=0.5, rely=0.59, anchor='center')

        # Image center

        img_center = Image.open(img_path_center11)
        self.img_center = CTkImage(img_center, size=(
            img_center.width, img_center.height))

        self.image_label_center = customtkinter.CTkLabel(
            self.box_options, image=self.img_center, text='')
        self.image_label_center.place(relx=0.5, rely=0.15, anchor='center')

        # Previous button
        self.button_prev = customtkinter.CTkButton(self.box_options, text='<', command=self.button_prev,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_prev.place(relx=0.13, rely=0.93, anchor='center')

        # Question box
        self.box_question = customtkinter.CTkFrame(
            self.box_options, width=304, height=80, fg_color="#EC9B9B", corner_radius=20)
        self.box_question.place(relx=0.5, rely=0.37, anchor='center')

        self.label_quest1 = customtkinter.CTkLabel(self.box_question, text="Apakah Anda mengalami  ", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest1.place(relx=0.5, rely=0.20, anchor='center')
        self.label_quest2 = customtkinter.CTkLabel(self.box_question, text="penurunan atau kenaikan", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest2.place(relx=0.5, rely=0.505, anchor='center')
        self.label_quest3 = customtkinter.CTkLabel(self.box_question, text="berat badan yang ekstrem?", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest3.place(relx=0.5, rely=0.8, anchor='center')
        self.selected_option = None  # Store the selected option

        # Buttons
        self.button_1 = customtkinter.CTkButton(self.box_options, text='Ya', command=self.button_1_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_1.place(relx=0.5, rely=0.55, anchor='center')

        self.button_2 = customtkinter.CTkButton(self.box_options, text='Tidak', command=self.button_2_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_2.place(relx=0.5, rely=0.70, anchor='center')

        # Next button
        self.button_next = customtkinter.CTkButton(self.box_options, text='>', command=self.button_next,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_next.place(relx=0.87, rely=0.93, anchor='center')

    # Load gambar

    def button_prev(self):
        self.master.switch_frame(Gejala9)

    def button_next(self):
        if self.selected_option != None:
            answers_gejala['gejala10'] = self.selected_option
            self.master.switch_frame(Gejala11)
            print(answers_gejala)

    def button_1_action(self):
        self.selected_option = 1
        self.update_button_colors()
        # print("Anda memilih ya.")

    def button_2_action(self):
        self.selected_option = 0
        self.update_button_colors()
        # print("Anda memilih ya.")

    def update_button_colors(self):
        self.button_1.configure(
            fg_color="#FFFAF1" if self.selected_option != 1 else "#F8B5BB")
        self.button_2.configure(
            fg_color="#FFFAF1" if self.selected_option != 0 else "#F8B5BB")


class Gejala11(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)
        self.master = master  # Save reference to the master
        self.configure(fg_color="#FFFAF1")

        # Title box
        self.box_title = customtkinter.CTkFrame(
            self, width=140, height=42, fg_color="#EC9B9B", corner_radius=13)
        self.box_title.place(relx=0.22, rely=0.07, anchor='center')

        self.label_title = customtkinter.CTkLabel(self.box_title, text="Prediksi Aktivitas", fg_color='transparent', text_color='#FFFFFF',
                                                  font=customtkinter.CTkFont(family='Roboto', size=15, weight='bold'))
        self.label_title.place(relx=0.5, rely=0.5, anchor='center')

        # Image initialization
        img_hover1 = Image.open(img_path_hover1)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(relx=0.94, rely=0.005, anchor='center')

        # Option box
        self.box_options = customtkinter.CTkFrame(
            self, width=350, height=520, fg_color="#F8DDDD", corner_radius=33)
        self.box_options.place(relx=0.5, rely=0.59, anchor='center')

        # Image center

        img_center = Image.open(img_path_center12)
        self.img_center = CTkImage(img_center, size=(
            img_center.width, img_center.height))

        self.image_label_center = customtkinter.CTkLabel(
            self.box_options, image=self.img_center, text='')
        self.image_label_center.place(relx=0.5, rely=0.18, anchor='center')

        # Previous button
        self.button_prev = customtkinter.CTkButton(self.box_options, text='<', command=self.button_prev,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_prev.place(relx=0.13, rely=0.93, anchor='center')

        # Question box
        self.box_question = customtkinter.CTkFrame(
            self.box_options, width=304, height=80, fg_color="#EC9B9B", corner_radius=20)
        self.box_question.place(relx=0.5, rely=0.37, anchor='center')

        self.label_quest1 = customtkinter.CTkLabel(self.box_question, text="Bagaimana Rutinitas Harian", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest1.place(relx=0.5, rely=0.32, anchor='center')
        self.label_quest2 = customtkinter.CTkLabel(self.box_question, text="Anda? ", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest2.place(relx=0.5, rely=0.67, anchor='center')

        self.selected_option = None  # Store the selected option

        # Buttons
        self.button_1 = customtkinter.CTkButton(self.box_options, text='Pasif bergerak', command=self.button_1_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_1.place(relx=0.5, rely=0.55, anchor='center')

        self.button_2 = customtkinter.CTkButton(self.box_options, text='Aktif bergerak', command=self.button_2_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_2.place(relx=0.5, rely=0.70, anchor='center')

        # Next button
        self.button_next = customtkinter.CTkButton(self.box_options, text='>', command=self.button_next,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_next.place(relx=0.87, rely=0.93, anchor='center')

    # Load gambar

    def button_prev(self):
        self.master.switch_frame(Gejala10)

    def button_next(self):
        if self.selected_option != None:
            answers_gejala['gejala11'] = self.selected_option
            self.master.switch_frame(Gejala12)
            print(answers_gejala)

    def button_1_action(self):
        self.selected_option = 1
        self.update_button_colors()
        # print("Anda memilih ya.")

    def button_2_action(self):
        self.selected_option = 0
        self.update_button_colors()
        # print("Anda memilih ya.")

    def update_button_colors(self):
        self.button_1.configure(
            fg_color="#FFFAF1" if self.selected_option != 1 else "#F8B5BB")
        self.button_2.configure(
            fg_color="#FFFAF1" if self.selected_option != 0 else "#F8B5BB")


class Gejala12(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)
        self.master = master  # Save reference to the master
        self.configure(fg_color="#FFFAF1")

        # Title box
        self.box_title = customtkinter.CTkFrame(
            self, width=140, height=42, fg_color="#EC9B9B", corner_radius=13)
        self.box_title.place(relx=0.22, rely=0.07, anchor='center')

        self.label_title = customtkinter.CTkLabel(self.box_title, text="Prediksi Aktivitas", fg_color='transparent', text_color='#FFFFFF',
                                                  font=customtkinter.CTkFont(family='Roboto', size=15, weight='bold'))
        self.label_title.place(relx=0.5, rely=0.5, anchor='center')

        # Image initialization
        img_hover1 = Image.open(img_path_hover1)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(relx=0.94, rely=0.005, anchor='center')

        # Option box
        self.box_options = customtkinter.CTkFrame(
            self, width=350, height=520, fg_color="#F8DDDD", corner_radius=33)
        self.box_options.place(relx=0.5, rely=0.59, anchor='center')

        # Image center
        img_center = Image.open(img_path_center13)
        self.img_center = CTkImage(img_center, size=(
            img_center.width, img_center.height))

        self.image_label_center = customtkinter.CTkLabel(
            self.box_options, image=self.img_center, text='')
        self.image_label_center.place(relx=0.5, rely=0.15, anchor='center')

        # Previous button
        self.button_prev = customtkinter.CTkButton(self.box_options, text='<', command=self.button_prev,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_prev.place(relx=0.13, rely=0.93, anchor='center')

        # Question box
        self.box_question = customtkinter.CTkFrame(
            self.box_options, width=304, height=80, fg_color="#EC9B9B", corner_radius=20)
        self.box_question.place(relx=0.5, rely=0.37, anchor='center')

        self.label_quest1 = customtkinter.CTkLabel(self.box_question, text="Seberapa sering Anda  ", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest1.place(relx=0.5, rely=0.20, anchor='center')
        self.label_quest2 = customtkinter.CTkLabel(self.box_question, text="Berolahraga dalam ", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest2.place(relx=0.5, rely=0.505, anchor='center')
        self.label_quest3 = customtkinter.CTkLabel(self.box_question, text="satu minggu?", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest3.place(relx=0.5, rely=0.8, anchor='center')
        self.selected_option = None  # Store the selected option

        # Buttons
        self.button_1 = customtkinter.CTkButton(self.box_options, text='Kurang dari 2 kali', command=self.button_1_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_1.place(relx=0.5, rely=0.55, anchor='center')

        self.button_2 = customtkinter.CTkButton(self.box_options, text='2 kali atau lebih', command=self.button_2_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_2.place(relx=0.5, rely=0.70, anchor='center')

        # Next button
        self.button_next = customtkinter.CTkButton(self.box_options, text='>', command=self.button_next,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_next.place(relx=0.87, rely=0.93, anchor='center')

    # Load gambar

    def button_prev(self):
        self.master.switch_frame(Gejala11)

    def button_next(self):
        if self.selected_option != None:
            answers_gejala['gejala12'] = self.selected_option
            self.master.switch_frame(Gejala13)
            print(answers_gejala)

    def button_1_action(self):
        self.selected_option = 1
        self.update_button_colors()
        # print("Anda memilih ya.")

    def button_2_action(self):
        self.selected_option = 0
        self.update_button_colors()
        # print("Anda memilih ya.")

    def update_button_colors(self):
        self.button_1.configure(
            fg_color="#FFFAF1" if self.selected_option != 1 else "#F8B5BB")
        self.button_2.configure(
            fg_color="#FFFAF1" if self.selected_option != 0 else "#F8B5BB")


class Gejala13(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)
        self.master = master  # Save reference to the master
        self.configure(fg_color="#FFFAF1")

        # Title box
        self.box_title = customtkinter.CTkFrame(
            self, width=140, height=42, fg_color="#EC9B9B", corner_radius=13)
        self.box_title.place(relx=0.22, rely=0.07, anchor='center')

        self.label_title = customtkinter.CTkLabel(self.box_title, text="Prediksi Aktivitas", fg_color='transparent', text_color='#FFFFFF',
                                                  font=customtkinter.CTkFont(family='Roboto', size=15, weight='bold'))
        self.label_title.place(relx=0.5, rely=0.5, anchor='center')

        # Image initialization
        img_hover1 = Image.open(img_path_hover1)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(relx=0.94, rely=0.005, anchor='center')

        # Option box
        self.box_options = customtkinter.CTkFrame(
            self, width=350, height=520, fg_color="#F8DDDD", corner_radius=33)
        self.box_options.place(relx=0.5, rely=0.59, anchor='center')

        # Image center
        
        img_center = Image.open(img_path_center14)
        self.img_center = CTkImage(img_center, size=(
            img_center.width, img_center.height))

        self.image_label_center = customtkinter.CTkLabel(
            self.box_options, image=self.img_center, text='')
        self.image_label_center.place(relx=0.5, rely=0.18, anchor='center')

        # Previous button
        self.button_prev = customtkinter.CTkButton(self.box_options, text='<', command=self.button_prev,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_prev.place(relx=0.13, rely=0.93, anchor='center')

        # Question box
        self.box_question = customtkinter.CTkFrame(
            self.box_options, width=304, height=80, fg_color="#EC9B9B", corner_radius=20)
        self.box_question.place(relx=0.5, rely=0.37, anchor='center')

        self.label_quest1 = customtkinter.CTkLabel(self.box_question, text="Apakah Anda sering ", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest1.place(relx=0.5, rely=0.32, anchor='center')
        self.label_quest2 = customtkinter.CTkLabel(self.box_question, text="Merokok atau vape?", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest2.place(relx=0.5, rely=0.67, anchor='center')

        self.selected_option = None  # Store the selected option

        # Buttons
        self.button_1 = customtkinter.CTkButton(self.box_options, text='Ya', command=self.button_1_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_1.place(relx=0.5, rely=0.55, anchor='center')

        self.button_2 = customtkinter.CTkButton(self.box_options, text='Tidak', command=self.button_2_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_2.place(relx=0.5, rely=0.70, anchor='center')

        # Next button
        self.button_next = customtkinter.CTkButton(self.box_options, text='>', command=self.button_next,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_next.place(relx=0.87, rely=0.93, anchor='center')

    # Load gambar

    def button_prev(self):
        self.master.switch_frame(Gejala12)

    def button_next(self):
        if self.selected_option != None:
            answers_gejala['gejala13'] = self.selected_option
            self.master.switch_frame(Gejala14)
            print(answers_gejala)

    def button_1_action(self):
        self.selected_option = 1
        self.update_button_colors()
        # print("Anda memilih ya.")

    def button_2_action(self):
        self.selected_option = 0
        self.update_button_colors()
        # print("Anda memilih ya.")

    def update_button_colors(self):
        self.button_1.configure(
            fg_color="#FFFAF1" if self.selected_option != 1 else "#F8B5BB")
        self.button_2.configure(
            fg_color="#FFFAF1" if self.selected_option != 0 else "#F8B5BB")


class Gejala14(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)
        self.master = master  # Save reference to the master
        self.configure(fg_color="#FFFAF1")

        # Title box
        self.box_title = customtkinter.CTkFrame(
            self, width=140, height=42, fg_color="#EC9B9B", corner_radius=13)
        self.box_title.place(relx=0.22, rely=0.07, anchor='center')

        self.label_title = customtkinter.CTkLabel(self.box_title, text="Prediksi Aktivitas", fg_color='transparent', text_color='#FFFFFF',
                                                  font=customtkinter.CTkFont(family='Roboto', size=15, weight='bold'))
        self.label_title.place(relx=0.5, rely=0.5, anchor='center')

        # Image initialization
        img_hover1 = Image.open(img_path_hover1)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(relx=0.94, rely=0.005, anchor='center')

        # Option box
        self.box_options = customtkinter.CTkFrame(
            self, width=350, height=520, fg_color="#F8DDDD", corner_radius=33)
        self.box_options.place(relx=0.5, rely=0.59, anchor='center')

        # Image center
        img_center = Image.open(img_path_center15)
        self.img_center = CTkImage(img_center, size=(
            img_center.width, img_center.height))

        self.image_label_center = customtkinter.CTkLabel(
            self.box_options, image=self.img_center, text='')
        self.image_label_center.place(relx=0.5, rely=0.15, anchor='center')

        # Previous button
        self.button_prev = customtkinter.CTkButton(self.box_options, text='<', command=self.button_prev,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_prev.place(relx=0.13, rely=0.93, anchor='center')

        # Question box
        self.box_question = customtkinter.CTkFrame(
            self.box_options, width=304, height=80, fg_color="#EC9B9B", corner_radius=20)
        self.box_question.place(relx=0.5, rely=0.37, anchor='center')

        self.label_quest1 = customtkinter.CTkLabel(self.box_question, text="Seberapa sering Anda  ", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest1.place(relx=0.5, rely=0.20, anchor='center')
        self.label_quest2 = customtkinter.CTkLabel(self.box_question, text="mengonsumsi Alkohol", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest2.place(relx=0.5, rely=0.505, anchor='center')
        self.label_quest3 = customtkinter.CTkLabel(self.box_question, text="dalam satu bulan?", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest3.place(relx=0.5, rely=0.8, anchor='center')
        self.selected_option = None  # Store the selected option

        # Buttons
        self.button_1 = customtkinter.CTkButton(self.box_options, text='Kurang dari 1 kali', command=self.button_1_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_1.place(relx=0.5, rely=0.55, anchor='center')

        self.button_2 = customtkinter.CTkButton(self.box_options, text='1 kali atau lebih', command=self.button_2_action,
                                                fg_color="#FFFAF1", text_color='#C14856',
                                                font=customtkinter.CTkFont(
                                                    family='Roboto', size=20, weight='bold'),
                                                height=55, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_2.place(relx=0.5, rely=0.70, anchor='center')

        # Next button
        self.button_next = customtkinter.CTkButton(self.box_options, text='>', command=self.button_next,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_next.place(relx=0.87, rely=0.93, anchor='center')

    # Load gambar

    def button_prev(self):
        self.master.switch_frame(Gejala13)

    def button_next(self):
        if self.selected_option != None:
            answers_gejala['gejala14'] = self.selected_option
            self.master.switch_frame(SeeResult)
            print(answers_gejala)

    def button_1_action(self):
        self.selected_option = 0
        self.update_button_colors()
        # print("Anda memilih ya.")

    def button_2_action(self):
        self.selected_option = 1
        self.update_button_colors()
        # print("Anda memilih ya.")

    def update_button_colors(self):
        self.button_1.configure(
            fg_color="#FFFAF1" if self.selected_option != 0 else "#F8B5BB")
        self.button_2.configure(
            fg_color="#FFFAF1" if self.selected_option != 1 else "#F8B5BB")


# count all risk
def count_risk_All():
    if answers_fisikGenetikaGlukosa['question5'] == 1:
        risiko_fisikdanGenetika = float(check_riskQuetion())

        # rules Glukosa
        glukosa = float(answers_fisikGenetikaGlukosa['question6'])
        if answers_fisikGenetikaGlukosa['question1'] == 1:
            if glukosa <= 130:
                res_glukosa = 0
            elif glukosa > 130:
                res_glukosa = 1
        elif answers_fisikGenetikaGlukosa['question1'] == 2:
            if glukosa <= 160:
                res_glukosa = 0
            elif glukosa > 160:
                res_glukosa = 1
        elif answers_fisikGenetikaGlukosa['question1'] == 3:
            if glukosa <= 150:
                res_glukosa = 0
            elif glukosa > 150:
                res_glukosa = 1

        risiko_glukosa = res_glukosa
        risiko_gejala = float(sum(answers_gejala.values()))

        # count bobot risiko
        bobot_fisikGenetika = float(risiko_fisikdanGenetika) * (15)
        print(bobot_fisikGenetika)
        bobot_glukosa = risiko_glukosa*(15)
        print(bobot_glukosa)
        bobot_gejala = risiko_gejala*(5)
        print(bobot_gejala)
        
        totalBobot = bobot_fisikGenetika+bobot_glukosa+bobot_gejala
    elif answers_fisikGenetikaGlukosa['question5'] == 0:
        risiko_fisikdanGenetika = float(check_riskQuetion())
        risiko_gejala = sum(answers_gejala.values())

        # count bobot risiko
        bobot_fisikGenetika = float(risiko_fisikdanGenetika) * (15)
        print(bobot_fisikGenetika)
        bobot_gejala = risiko_gejala*(5)
        print(bobot_gejala)
        totalBobot = bobot_fisikGenetika+bobot_gejala
    print(totalBobot)
    return totalBobot

# clasification risk rule


def classification_risk(count_risk_All):
    classification = None
    if answers_fisikGenetikaGlukosa['question5'] == 1:
        if count_risk_All <= (25):
            classification = 'Batas Toleransi'
        elif (26) <= count_risk_All and count_risk_All <= (50):
            classification = 'Berpotensi Rendah'
        elif (51) <= count_risk_All and count_risk_All <= (75):
            classification = 'Berpotensi Sedang'
        elif (76) <= count_risk_All and count_risk_All <= (100):
            classification = 'Berpotensi Tinggi'
    elif answers_fisikGenetikaGlukosa['question5'] == 0:
        if count_risk_All <= (25):
            classification = 'Batas Toleransi'
        elif (26) <= count_risk_All and count_risk_All <= (45):
            classification = 'Berpotensi Rendah'
        elif (46) <= count_risk_All and count_risk_All <= (65):
            classification = 'Berpotensi Sedang'
        elif (66) <= count_risk_All and count_risk_All <= (85):
            classification = 'Berpotensi Tinggi'
    return classification

# UI Result


class SeeResult(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)
        self.master = master  # Save reference to the master
        self.configure(fg_color="#FFFAF1")

        # Image initialization
        img_hover1 = Image.open(img_path_hover1)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(relx=0.94, rely=0.005, anchor='center')

        # Option box
        self.box_options = customtkinter.CTkFrame(
            self, width=350, height=520, fg_color="#F8DDDD", corner_radius=33)
        self.box_options.place(relx=0.5, rely=0.59, anchor='center')

        # Image center
        img_center = Image.open(img_path_centerCR)
        self.img_center = CTkImage(img_center, size=(
            img_center.width, img_center.height))

        self.image_label_center = customtkinter.CTkLabel(
            self.box_options, image=self.img_center, text='')
        self.image_label_center.place(relx=0.5, rely=0.85, anchor='center')

        # Previous button
        self.button_prev = customtkinter.CTkButton(self, text='<', command=self.button_prev,
                                                   fg_color="#F8B5BB", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=51,
                                                   width=65,
                                                   corner_radius=25,
                                                   hover_color='#F8B5BB')
        self.button_prev.place(relx=0.1, rely=0.05,
                               anchor=customtkinter.CENTER)

        # Question box
        self.box_question = customtkinter.CTkFrame(
            self.box_options, width=304, height=80, fg_color="#DC6874", corner_radius=20)
        self.box_question.place(relx=0.5, rely=0.2, anchor='center')

        self.label_quest1 = customtkinter.CTkLabel(self.box_question, text="Anda Telah mengisi ", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest1.place(relx=0.5, rely=0.32, anchor='center')
        self.label_quest2 = customtkinter.CTkLabel(self.box_question, text="semuanya", fg_color='transparent', text_color='#FFFFFF',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest2.place(relx=0.5, rely=0.67, anchor='center')

        self.selected_option = None  # Store the selected option

        # Buttons
        self.button_seeResult = customtkinter.CTkButton(self.box_options, text='Lihat Hasil Prediksi', command=self.button_seeResult_action,
                                                        fg_color="#FFFAF1", text_color='#C14856',
                                                        font=customtkinter.CTkFont(
                                                            family='Roboto', size=20, weight='bold'),
                                                        height=85, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_seeResult.place(relx=0.5, rely=0.45, anchor='center')

        self.button_Home = customtkinter.CTkButton(self.box_options, text='Home', command=self.button_home_action,
                                                   fg_color="#FFFAF1", text_color='#C14856',
                                                   font=customtkinter.CTkFont(
                                                       family='Roboto', size=20, weight='bold'),
                                                   height=85, width=260, corner_radius=25, hover_color='#F8B5BB')
        self.button_Home.place(relx=0.5, rely=0.65, anchor='center')

    # Load gambar

    def button_prev(self):
        self.master.switch_frame(Gejala14)

    def button_seeResult_action(self):
        self.master.switch_frame(ResultPage)
        print(answers_gejala)

    def button_home_action(self):
        self.master.switch_frame(Home)
        print(answers_gejala)


class ResultPage(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)

        # gambar hover
        img_hover1 = Image.open(img_path_hoverHR)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(relx=0.15, rely=0.96, anchor=CENTER)
        self.image_label_hover1.configure(bg_color='transparent')

        img_hover2 = Image.open(img_path_hoverHR)
        self.img_hover2 = CTkImage(img_hover2, size=(
            img_hover2.width, img_hover2.height))

        self.image_label_hover2 = customtkinter.CTkLabel(
            self, image=self.img_hover2, text='')
        self.image_label_hover2.place(relx=0.88, rely=0.002, anchor=CENTER)
        self.image_label_hover2.configure(bg_color='transparent')

        # Option box
        self.box_options = customtkinter.CTkFrame(
            self, width=350, height=380, fg_color="#F8DDDD", corner_radius=33)
        self.box_options.place(relx=0.5, rely=0.48, anchor='center')
        self.configure(fg_color="#C14856")
        self.configure(bg_color='transparent')

        # Image center
        img_center = Image.open(img_path_centerRP)
        self.img_center = CTkImage(img_center, size=(
            img_center.width, img_center.height))

        self.image_label_center = customtkinter.CTkLabel(
            self.box_options, image=self.img_center, text='')
        self.image_label_center.place(relx=0.5, rely=0.35, anchor='center')

        # Question box
        self.box_question = customtkinter.CTkFrame(
            self.box_options, width=304, height=60, fg_color="#FFFAF1", corner_radius=20)
        self.box_question.place(relx=0.5, rely=0.13, anchor='center')

        self.label_quest1 = customtkinter.CTkLabel(self.box_question, text="Hasil Prediksi Diri Anda ", fg_color='transparent', text_color='#C14856',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest1.place(relx=0.5, rely=0.5, anchor='center')

        # Question box
        self.box_result = customtkinter.CTkFrame(
            self.box_options, width=304, height=120, fg_color="#A62332", corner_radius=20)
        self.box_result.place(relx=0.5, rely=0.65, anchor='center')

        self.label_pred1 = customtkinter.CTkLabel(self.box_result, text=f"Anda Berisiko Diabetes", fg_color='transparent', text_color='#FFFAF1',
                                                  font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_pred1.place(relx=0.5, rely=0.18, anchor='center')

        self.label_percent = customtkinter.CTkLabel(self.box_result, text=f"{(round(count_risk_All(),2))} % ", fg_color='#FFFAF1', text_color='#C14856',
                                                    width=150, height=40, corner_radius=20,
                                                    font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_percent.place(relx=0.5, rely=0.5, anchor='center')


        self.label_pred2 = customtkinter.CTkLabel(self.box_result, text=f"{classification_risk(round(count_risk_All(),2))}", fg_color='transparent', text_color='#FFFAF1',
                                                  font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_pred2.place(relx=0.5, rely=0.82, anchor='center')

        # Buttons
        self.button_saran = customtkinter.CTkButton(self.box_options, text='Saran Preventif', command=self.button_saran_action,
                                                    fg_color="#C14856", text_color='#FFFAF1',
                                                    font=customtkinter.CTkFont(
                                                        family='Roboto', size=20, weight='bold'),
                                                    height=50, width=100, corner_radius=25, hover_color='#F8B5BB')
        self.button_saran.place(relx=0.5, rely=0.9, anchor='center')

    def button_saran_action(self):
        self.master.switch_frame(SaranPage)
        print(classification_risk(round(count_risk_All(), 2)))


def resultSaran():
    saran = []
    if answers_gejala['gejala1'] == 1:
        saran.append("Perbanyak minum air mineral")
    if answers_gejala['gejala2'] == 1:
        saran.append("Kurangi makan di luar jam")
    if answers_gejala['gejala11'] == 1:
        saran.append("Lakukan gerakan ringan sesekali")
    if answers_gejala['gejala12'] == 1:
        saran.append("Olahraga minimal 2 kali perminggu")
    if answers_gejala['gejala13'] == 1:
        saran.append("Kurangi atau berhenti merokok")
    if answers_gejala['gejala14'] == 1:
        saran.append("Kurangi/berhenti konsumsi Alkohol")

    if not saran:
        saran.append("Tetap lakukan gaya hidup sehat")

    return "- Kurangi konsumi gula\n" + "\n".join(f"- {item}" for item in saran)


# UI SaranPage
class SaranPage(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)

        # gambar hover
        img_hover1 = Image.open(img_path_hoverHR)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(relx=0.15, rely=0.96, anchor=CENTER)
        self.image_label_hover1.configure(bg_color='transparent')

        img_hover2 = Image.open(img_path_hoverHR)
        self.img_hover2 = CTkImage(img_hover2, size=(
            img_hover2.width, img_hover2.height))

        self.image_label_hover2 = customtkinter.CTkLabel(
            self, image=self.img_hover2, text='')
        self.image_label_hover2.place(relx=0.88, rely=0.002, anchor=CENTER)
        self.image_label_hover2.configure(bg_color='transparent')

        # Option box
        self.box_options = customtkinter.CTkFrame(
            self, width=350, height=380, fg_color="#F8DDDD", corner_radius=33)
        self.box_options.place(relx=0.5, rely=0.48, anchor='center')
        self.configure(fg_color="#C14856")
        self.configure(bg_color='transparent')

        # Question box
        self.box_question = customtkinter.CTkFrame(
            self.box_options, width=304, height=50, fg_color="#FFFAF1", corner_radius=20)
        self.box_question.place(relx=0.5, rely=0.11, anchor='center')

        self.label_quest1 = customtkinter.CTkLabel(self.box_question, text="Saran Aktivitas", fg_color='transparent', text_color='#C14856',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest1.place(relx=0.5, rely=0.5, anchor='center')

        # Question box
        self.box_result = customtkinter.CTkFrame(
            self.box_options, width=304, height=200, fg_color="#A62332", corner_radius=20)
        self.box_result.place(relx=0.5, rely=0.51, anchor='center')

        self.label_saran = customtkinter.CTkLabel(self.box_result, text=f'{resultSaran()}', fg_color='transparent', text_color='#FFFAF1',
                                                  font=customtkinter.CTkFont(family='Roboto', size=16, weight='bold'), justify='left')
        self.label_saran.place(relx=0.5, rely=0.5, anchor='center')

        # Buttons
        self.button_Out = customtkinter.CTkButton(self.box_options, text='Selanjutnya', command=self.button_out_action,
                                                  fg_color="#C14856", text_color='#FFFAF1',
                                                  font=customtkinter.CTkFont(
                                                      family='Roboto', size=20, weight='bold'),
                                                  height=50, width=100, corner_radius=25, hover_color='#F8B5BB')
        self.button_Out.place(relx=0.5, rely=0.9, anchor='center')

    def button_out_action(self):
        self.master.switch_frame(SaranObat)
        print(classification_risk(round(count_risk_All(), 2)))


# UI SaranObat

def get_label(instance):
    labels = []
    if hasattr(instance, 'label_quest1') and instance.label_quest1.cget("text") != None:
        labels.append(instance.label_quest1.cget("text"))
    else:
        labels.append("")

    if hasattr(instance, 'label_quest2') and instance.label_quest2.cget("text") != None: 
        labels.append(instance.label_quest2.cget("text"))
    else:
        labels.append("")
    
    if hasattr(instance, 'label_quest3') and instance.label_quest3.cget("text") != None:
        labels.append(instance.label_quest3.cget("text"))
    else:
        labels.append("")
    
    return " ".join(labels)
        
def user_sympthom(master):
    symthom =[]
    for i in range (1, len(answers_gejala) +1):
        if answers_gejala[f'gejala{i}'] == 1:
            questGejalaClass = globals().get(f'Gejala{i}', None)
            if questGejalaClass:  
                questGejala = questGejalaClass(master)
                symthom.append(get_label(questGejala))
    return symthom
        
        
def result_drugs_recommendation(master):
    path_rulesDrugs = os.path.join(root_directory,"Aplication", "Rule", "data_gejala_obat.csv")
    df = pd.read_csv(path_rulesDrugs)
    
    rulesCorpus = df["Gejala"].tolist()
    user_sympCorpus = user_sympthom(master)
    print(user_sympCorpus)

    combined_corpus = rulesCorpus + user_sympCorpus

    vectorizer = TfidfVectorizer()
    tfidf_combined = vectorizer.fit_transform(combined_corpus)

    tfidf_rules = tfidf_combined[:len(rulesCorpus)]
    tfidf_userSym = tfidf_combined[len(rulesCorpus):]

    similarities = cosine_similarity(tfidf_userSym, tfidf_rules)
    
    max_index = similarities[0].argmax()
    recommended_drug = df.iloc[max_index]["Obat"]
    similarity_score = similarities[0][max_index]
    print(similarity_score)
    return recommended_drug

class SaranObat(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)

        # gambar hover
        img_hover1 = Image.open(img_path_hoverHR)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(relx=0.15, rely=0.96, anchor=CENTER)
        self.image_label_hover1.configure(bg_color='transparent')

        img_hover2 = Image.open(img_path_hoverHR)
        self.img_hover2 = CTkImage(img_hover2, size=(
            img_hover2.width, img_hover2.height))

        self.image_label_hover2 = customtkinter.CTkLabel(
            self, image=self.img_hover2, text='')
        self.image_label_hover2.place(relx=0.88, rely=0.002, anchor=CENTER)
        self.image_label_hover2.configure(bg_color='transparent')

        # Option box
        self.box_options = customtkinter.CTkFrame(
            self, width=350, height=380, fg_color="#F8DDDD", corner_radius=33)
        self.box_options.place(relx=0.5, rely=0.48, anchor='center')
        self.configure(fg_color="#C14856")
        self.configure(bg_color='transparent')

        # Question box
        self.box_question = customtkinter.CTkFrame(
            self.box_options, width=304, height=50, fg_color="#FFFAF1", corner_radius=20)
        self.box_question.place(relx=0.5, rely=0.11, anchor='center')

        self.label_quest1 = customtkinter.CTkLabel(self.box_question, text="Saran Obat", fg_color='transparent', text_color='#C14856',
                                                   font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label_quest1.place(relx=0.5, rely=0.5, anchor='center')

        # Question box
        self.box_result = customtkinter.CTkFrame(
            self.box_options, width=304, height=200, fg_color="#A62332", corner_radius=20)
        self.box_result.place(relx=0.5, rely=0.51, anchor='center')

        self.label_saran = customtkinter.CTkLabel(self.box_result, text=f'{result_drugs_recommendation(master)}', fg_color='transparent', text_color='#FFFAF1',
                                                  font=customtkinter.CTkFont(family='Roboto', size=16, weight='bold'), justify='left')
        self.label_saran.place(relx=0.5, rely=0.5, anchor='center')

        # Buttons
        self.button_Out = customtkinter.CTkButton(self.box_options, text='Keluar', command=self.button_out_action,
                                                  fg_color="#C14856", text_color='#FFFAF1',
                                                  font=customtkinter.CTkFont(
                                                      family='Roboto', size=20, weight='bold'),
                                                  height=50, width=100, corner_radius=25, hover_color='#F8B5BB')
        self.button_Out.place(relx=0.5, rely=0.9, anchor='center')

    def button_out_action(self):
        self.master.switch_frame(Home)
        print(classification_risk(round(count_risk_All(), 2)))

# UI Home Page

class Home(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=375, height=667)

        self.label1 = customtkinter.CTkLabel(self, text="Cek Risiko", text_color='#FDF9F1',
                                             font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label1.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.label2 = customtkinter.CTkLabel(self, text="Diabetes Yuk", text_color='#FDF9F1',
                                             font=customtkinter.CTkFont(family='Roboto', size=20, weight='bold'))
        self.label2.place(relx=0.5, rely=0.54, anchor=CENTER)

        self.button = customtkinter.CTkButton(self, text='Cek Sekarang', command=self.button_event,
                                              fg_color="#FDF9F1", text_color='#C14856',
                                              font=customtkinter.CTkFont(
                                                  family='Roboto', size=20, weight='bold'),
                                              width=219,
                                              height=51,
                                              corner_radius=25,
                                              hover_color='#FDF9F1')
        self.button.place(relx=0.5, rely=0.63, anchor=CENTER)
        self.configure(fg_color="#C14856")

        # gambar home
        img_center = Image.open(img_path_centerHOME)
        self.img_center = CTkImage(img_center, size=(
            img_center.width, img_center.height))

        self.image_label_center = customtkinter.CTkLabel(
            self, image=self.img_center, text='')
        self.image_label_center.place(relx=0.5, rely=0.35, anchor=CENTER)

        # gambar hover
        img_hover1 = Image.open(img_path_hover1)
        self.img_hover1 = CTkImage(img_hover1, size=(
            img_hover1.width, img_hover1.height))

        self.image_label_hover1 = customtkinter.CTkLabel(
            self, image=self.img_hover1, text='')
        self.image_label_hover1.place(relx=0.15, rely=0.96, anchor=CENTER)

        img_hover2 = Image.open(img_path_hover1)
        self.img_hover2 = CTkImage(img_hover2, size=(
            img_hover2.width, img_hover2.height))

        self.image_label_hover2 = customtkinter.CTkLabel(
            self, image=self.img_hover2, text='')
        self.image_label_hover2.place(relx=0.88, rely=0.002, anchor=CENTER)

    def button_event(self):
        # Access switch_frame from master (App)
        self.master.switch_frame(Question1)

# Master Window App

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("375x667")
        self.title('Cek Risiko Diabetes')
        self.switch_frame(Home)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if hasattr(self, 'current_frame'):
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
