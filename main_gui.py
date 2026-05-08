import customtkinter as ctk
from tkinter import filedialog
import threading

from processor import (
    start_parallel_processing,
    start_sequential_processing
)


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class HPFDP_App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("HPFDP - High Performance Financial Data Processor")
        self.geometry("700x600")

        self.selected_file = None
        self.seq_time_cached = None

        self.build_ui()
        
    def build_ui(self):

        title = ctk.CTkLabel(
            self,
            text="HPFDP System",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=25)

        subtitle = ctk.CTkLabel(
            self,
            text="Layered Architecture + Design Patterns",
            font=("Arial", 14),
            text_color="cyan"
        )
        subtitle.pack(pady=5)
            
        self.select_btn = ctk.CTkButton(
        self,
        text="Select CSV File",
        command=self.select_file
    )
        self.select_btn.pack(pady=15)

        self.file_path_label = ctk.CTkLabel(
            self,
            text="No file selected",
            text_color="gray"
        )
        self.file_path_label.pack(pady=5)

        self.start_par_btn = ctk.CTkButton(
            self,
            text="Start Parallel Processing",
            fg_color="green",
            state="disabled",
            command=lambda: self.run_process_thread("parallel")
        )
        
        self.start_par_btn.pack(pady=10)

        self.start_seq_btn = ctk.CTkButton(
            self,
            text="Start Sequential Processing",
            fg_color="orange",
            text_color="black",
            state="disabled",
            command=lambda: self.run_process_thread("sequential")
        )
        self.start_seq_btn.pack(pady=10)

        self.progress_bar = ctk.CTkProgressBar(
            self,
            width=450
        )
        
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=25)

        self.status_label = ctk.CTkLabel(
            self,
            text="Status: Ready",
            font=("Arial", 14)
        )
        self.status_label.pack(pady=10)
        
        self.comparison_label = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 15, "italic"),
            text_color="cyan"
        )
        self.comparison_label.pack(pady=20)
        
    def select_file(self):

        file_path = filedialog.askopenfilename(
            filetypes=[("CSV Files", "*.csv")]
        )

        if file_path:
            self.selected_file = file_path

            self.file_path_label.configure(
                text=file_path,
                text_color="white"
            )

            self.start_par_btn.configure(state="normal")
            self.start_seq_btn.configure(state="normal")

            self.comparison_label.configure(text="")
                
    def run_process_thread(self, mode):

        self.start_par_btn.configure(state="disabled")
        self.start_seq_btn.configure(state="disabled")

        self.progress_bar.start()

        if mode == "parallel":
            self.status_label.configure(
                text="Processing in Parallel...",
                text_color="yellow"
            )
        else:
            self.status_label.configure(
                text="Processing Sequentially...",
                text_color="orange"
            )

        thread = threading.Thread(
            target=self.execute_batch,
            args=(mode,)
        )

        thread.start()
        
    def execute_batch(self, mode):

        try:

            if mode == "parallel":

                total, duration = start_parallel_processing(
                    self.selected_file
                )

                self.status_label.configure(
                    text=f"SUCCESS (Parallel): {total} rows in {duration}s",
                    text_color="green"
                )

                if self.seq_time_cached:
                    improvement = round(
                        (
                            (
                                self.seq_time_cached - duration
                            )
                            /
                            self.seq_time_cached
                        ) * 100,
                        2
                    )
                    self.comparison_label.configure(
                        text=f"Performance Gain: {improvement}% Faster"
                    )
            else:

                total, duration = start_sequential_processing(
                    self.selected_file
                )

                self.seq_time_cached = duration

                self.status_label.configure(
                    text=f"SUCCESS (Sequential): {total} rows in {duration}s",
                    text_color="green"
                )

                self.comparison_label.configure(
                    text="Sequential result saved. Run Parallel for comparison."
                )

        except Exception as e:
            self.status_label.configure(
                text="ERROR: Processing Failed",
                text_color="red"
            )

            print(f"Error Details: {e}")
        
        finally:

            self.progress_bar.stop()
            self.progress_bar.set(1)

            self.start_par_btn.configure(state="normal")
            self.start_seq_btn.configure(state="normal")
            
if __name__ == "__main__":
    app = HPFDP_App()
    app.mainloop()
            
        