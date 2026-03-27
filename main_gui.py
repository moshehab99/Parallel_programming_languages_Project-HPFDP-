import customtkinter as ctk
from tkinter import filedialog
import threading
from processor import start_batch_processing # بنستدعي الكود اللي أنت لسه عامله

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class HPFDP_App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("HPFDP - High Performance Processor")
        self.geometry("600x450")

        # UI Elements
        self.label = ctk.CTkLabel(self, text="Financial Data Processor (Parallel)", font=("Arial", 22, "bold"))
        self.label.pack(pady=30)

        self.select_btn = ctk.CTkButton(self, text="Select CSV File", command=self.select_file)
        self.select_btn.pack(pady=10)

        self.file_path_label = ctk.CTkLabel(self, text="No file selected", text_color="gray")
        self.file_path_label.pack(pady=5)

        self.start_btn = ctk.CTkButton(self, text="Start Batch Processing", state="disabled", 
                                       fg_color="green", command=self.run_process_thread)
        self.start_btn.pack(pady=20)

        self.progress_bar = ctk.CTkProgressBar(self, width=400)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=20)

        self.status_label = ctk.CTkLabel(self, text="Status: Ready", text_color="white")
        self.status_label.pack(pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.file_path_label.configure(text=file_path, text_color="white")
            self.start_btn.configure(state="normal")
            self.selected_file = file_path

    def run_process_thread(self):
        # بنشغل المعالجة في Thread تاني عشان الواجهة متهنجش (Freeze)
        self.start_btn.configure(state="disabled")
        self.status_label.configure(text="Processing... Please wait", text_color="yellow")
        self.progress_bar.start()
        
        thread = threading.Thread(target=self.execute_batch)
        thread.start()

    def execute_batch(self):
        try:
            # بننادي على الدالة اللي في ملف processor.py
            start_batch_processing(self.selected_file)
            self.status_label.configure(text="SUCCESS: Data saved to MySQL", text_color="green")
        except Exception as e:
            self.status_label.configure(text=f"ERROR: {str(e)}", text_color="red")
        finally:
            self.progress_bar.stop()
            self.progress_bar.set(1)
            self.start_btn.configure(state="normal")

if __name__ == "__main__":
    app = HPFDP_App()
    app.mainloop()