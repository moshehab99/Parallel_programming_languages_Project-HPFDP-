import customtkinter as ctk
from tkinter import filedialog
import threading
from processor import start_parallel_processing, start_sequential_processing

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class HPFDP_App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("HPFDP - High Performance Processor")
        self.geometry("650x550") 

        self.label = ctk.CTkLabel(self, text="Financial Data Processor", font=("Arial", 24, "bold"))
        self.label.pack(pady=30)

        self.select_btn = ctk.CTkButton(self, text="Select CSV File", command=self.select_file)
        self.select_btn.pack(pady=10)

        self.file_path_label = ctk.CTkLabel(self, text="No file selected", text_color="gray")
        self.file_path_label.pack(pady=5)

        # زر لتشغيل البراليل (المشروع الأساسي)
        self.start_par_btn = ctk.CTkButton(self, text="Start Parallel Processing (Fast)", state="disabled", 
                                       fg_color="green", command=lambda: self.run_process_thread("parallel"))
        self.start_par_btn.pack(pady=10)

        # زر لتشغيل السكونشل (للمقارنة)
        self.start_seq_btn = ctk.CTkButton(self, text="Start Sequential Processing (Slow)", state="disabled", 
                                       fg_color="orange", text_color="black", command=lambda: self.run_process_thread("sequential"))
        self.start_seq_btn.pack(pady=10)

        self.progress_bar = ctk.CTkProgressBar(self, width=400)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=20)

        self.status_label = ctk.CTkLabel(self, text="Status: Ready", text_color="white")
        self.status_label.pack(pady=10)

        # جزء لإظهار المقارنة في الواجهة
        self.comparison_label = ctk.CTkLabel(self, text="", font=("Arial", 14, "italic"), text_color="cyan")
        self.comparison_label.pack(pady=20)
        self.seq_time_cached = None # لحفظ وقت السكونشل للمقارنة لاحقاً

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.file_path_label.configure(text=file_path, text_color="white")
            self.start_par_btn.configure(state="normal")
            self.start_seq_btn.configure(state="normal")
            self.selected_file = file_path
            self.comparison_label.configure(text="") # مسح المقارنة السابقة
            self.seq_time_cached = None

    def run_process_thread(self, mode):
        self.start_par_btn.configure(state="disabled")
        self.start_seq_btn.configure(state="disabled")
        status_text = "Processing in Parallel..." if mode == "parallel" else "Processing Sequentially..."
        status_color = "yellow" if mode == "parallel" else "orange"
        self.status_label.configure(text=status_text, text_color=status_color)
        self.progress_bar.start()
        
        # استخدام Threading هنا لمنع تجمد الواجهة (GUI Responsiveness)
        # الـ Multiprocessing بيحصل جوه الـ processor.py في الـ Backend
        thread = threading.Thread(target=self.execute_batch, args=(mode,))
        thread.start()

    def execute_batch(self, mode):
        try:
            if mode == "parallel":
                total, duration = start_parallel_processing(self.selected_file)
                self.status_label.configure(text=f"SUCCESS (Parallel): {total} rows in {duration}s", text_color="green")
                # إظهار المقارنة لو وقت السكونشل موجود
                if self.seq_time_cached:
                    improvement = round(((self.seq_time_cached - duration) / self.seq_time_cached) * 100, 2)
                    self.comparison_label.configure(text=f"Performance Gain: {improvement}% Faster than Sequential!")
            else:
                total, duration = start_sequential_processing(self.selected_file)
                self.status_label.configure(text=f"SUCCESS (Sequential): {total} rows in {duration}s", text_color="green")
                self.seq_time_cached = duration # حفظ الوقت للمقارنة
                self.comparison_label.configure(text="Sequential time cached. Run Parallel to see gain.")

        except Exception as e:
            self.status_label.configure(text=f"ERROR: Check Connection or File", text_color="red")
            print(f"Error details: {e}")
        finally:
            self.progress_bar.stop()
            self.progress_bar.set(1)
            self.start_par_btn.configure(state="normal")
            self.start_seq_btn.configure(state="normal")

if __name__ == "__main__":
    app = HPFDP_App()
    app.mainloop()