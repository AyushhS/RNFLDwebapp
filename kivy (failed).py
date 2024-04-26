from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.camera import Camera
import os

def image_processing():
     pass

class CameraApp(App):
     def build(self):
          self.image = Image()
          self.camera = Camera(play=True)
          self.file_chooser = FileChooserListView(path='/', filters=['*.png', '*.jpg', '*.jpeg'])
          self.upload_from_gallery_widget_ON = False
          self.camera_recapture = False
          self.gallery_recapture = False

          self.capture_from_camera_option_button = Button(text='Capture from Camera')
          self.capture_from_camera_option_button.bind(on_press=self.capture_from_camera)
          self.upload_from_gallery_option_button = Button(text='Upload from Gallery')
          self.upload_from_gallery_option_button.bind(on_press=self.upload_from_gallery)
          self.layout = BoxLayout(orientation='vertical')
          # self.layout.add_widget(self.image)
          # self.layout.add_widget(self.camera)
          self.layout.add_widget(self.capture_from_camera_option_button)
          self.layout.add_widget(self.upload_from_gallery_option_button)

          self.image_uploaded = True
          return self.layout

     def capture_from_camera(self, instance):
          if self.camera_recapture:
               self.layout.remove_widget(self.camera)
               self.layout.remove_widget(self.recapture_button)
               self.layout.remove_widget(self.image)
               self.layout.remove_widget(self.proceed_button)
          self.layout.remove_widget(self.capture_from_camera_option_button)
          self.layout.remove_widget(self.upload_from_gallery_option_button)
          self.layout.add_widget(self.camera)
          self.capture_button = Button(text='Capture')
          self.capture_button.bind(on_press=self.capture)
          self.layout.add_widget(self.capture_button)
          

     def capture(self, instance):
          self.camera.export_to_png('capture.png')
          self.image.source = 'capture.png'
          self.layout.remove_widget(self.camera)
          self.layout.remove_widget(self.capture_button)
          self.image.reload()
          self.layout.add_widget(self.image)

          # recapture functionality
          self.camera_recapture = True
          self.recapture_button = Button(text='recapture')
          self.recapture_button.bind(on_press=self.capture_from_camera)
          self.layout.add_widget(self.recapture_button)

          # Image processing proceed
          self.proceed_button = Button(text='Proceed')
          # self.proceed_button.bind(on_press=image_processing)
          self.layout.add_widget(self.proceed_button)

     def upload_from_gallery(self, instance):
          if self.gallery_recapture:
               self.layout.remove_widget(self.image)
               self.layout.remove_widget(self.recapture_button)
               self.layout.remove_widget(self.proceed_button)
          self.file_chooser.bind(on_submit=self.load_image)
          if not self.upload_from_gallery_widget_ON:
               self.layout.remove_widget(self.capture_from_camera_option_button)
               self.layout.remove_widget(self.upload_from_gallery_option_button)
               self.layout.add_widget(self.file_chooser)
          self.upload_from_gallery_widget_ON = True

     def load_image(self, instance, selection, touch=None):
          if selection:
               selected_image = selection[0]
               self.image.source = selected_image
          self.layout.remove_widget(instance)
          self.upload_from_gallery_widget_ON = False
          self.layout.add_widget(self.image)

          # recapture 
          self.recapture_button = Button(text='recapture')
          self.recapture_button.bind(on_press=self.upload_from_gallery)
          self.layout.add_widget(self.recapture_button)
          self.gallery_recapture = True

          # Image processing proceed
          self.proceed_button = Button(text='Proceed')
          # self.proceed_button.bind(on_press=image_processing)
          self.layout.add_widget(self.proceed_button)

if __name__ == '__main__':
     CameraApp().run()
