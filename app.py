import argparse,subprocess,sys,threading

def command(source,output): return [sys.executable,'-m','demucs','-n','htdemucs','-o',output,source]
def gui():
    import tkinter as tk
    from tkinter import filedialog
    root=tk.Tk();root.title('AI Audio Separator');status=tk.StringVar(value='Choose an audio file');tk.Label(root,textvariable=status).pack(padx=20,pady=20)
    def start():
        source=filedialog.askopenfilename();output=filedialog.askdirectory()
        if not source or not output:return
        button.config(state='disabled');status.set('Processing...')
        def work():
            try: subprocess.run(command(source,output),check=True);result='Done'
            except Exception as e: result=str(e)
            root.after(0,lambda:(status.set(result),button.config(state='normal')))
        threading.Thread(target=work,daemon=True).start()
    button=tk.Button(root,text='Separate audio',command=start);button.pack(pady=20);root.mainloop()
def main():
    p=argparse.ArgumentParser();p.add_argument('input',nargs='?');p.add_argument('--output',default='output');a=p.parse_args()
    if a.input: subprocess.run(command(a.input,a.output),check=True)
    else: gui()
if __name__=='__main__': main()
