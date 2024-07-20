import random
import smtplib
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox


# Function to generate a 6-digit OTP
def generate_otp():
    """Generates a random 6-digit OTP."""
    return random.randint(100000, 999999)


# Function to send OTP to user's email
def send_otp(email, otp):
    """
    Sends the OTP to the provided email address.
    Args:
        email (str): The recipient's email address.
        otp (int): The OTP to send.
    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """
    try:
        sender_email = "krishnakoturu26@gmail.com"
        sender_password = "maaw qtaw ioey ypjl"

        message = MIMEText(f"Your OTP is: {otp}")
        message['Subject'] = 'Your OTP Code'
        message['From'] = sender_email
        message['To'] = email

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, message.as_string())

        print(f"OTP sent to {email}")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False


# GUI Application
class OTPApp:
    def __init__(self, master):
        self.master = master
        self.master.title("OTP Verification System")
        self.otp = None
        self.attempts = 3

        self.label = tk.Label(master, text="Enter your email:")
        self.label.pack()

        self.email_entry = tk.Entry(master,width=35)
        self.email_entry.pack()

        self.send_button = tk.Button(master, text="Send OTP", command=self.send_otp)
        self.send_button.pack()

        self.label_otp = tk.Label(master, text="Enter OTP:")
        self.label_otp.pack()

        self.otp_entry = tk.Entry(master,width=35)
        self.otp_entry.pack()

        self.verify_button = tk.Button(master, text="Verify OTP", command=self.verify_otp)
        self.verify_button.pack()

    def send_otp(self):
        """Handles sending OTP to the user's email."""
        email = self.email_entry.get()
        if email:
            self.otp = generate_otp()
            if send_otp(email, self.otp):
                messagebox.showinfo("Success", "OTP sent to your email!")
            else:
                messagebox.showerror("Error", "Failed to send OTP. Please try again.")
        else:
            messagebox.showwarning("Input Error", "Please enter a valid email address.")

    def verify_otp(self):
        """Handles verification of the entered OTP."""
        entered_otp = self.otp_entry.get()
        if entered_otp.isdigit():
            if self.otp and int(entered_otp) == self.otp:
                messagebox.showinfo("Success", "OTP Verified Successfully!")
                self.master.destroy()
            else:
                self.attempts -= 1
                if self.attempts > 0:
                    messagebox.showerror("Error", f"Incorrect OTP. You have {self.attempts} attempts left.")
                else:
                    messagebox.showerror("Error", "You have exceeded the maximum number of attempts.")
                    self.master.destroy()
        else:
            messagebox.showwarning("Input Error", "Please enter a valid 6-digit OTP.")


if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(400,400)
    app = OTPApp(root)
    root.mainloop()
