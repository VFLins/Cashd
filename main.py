import prompter as ppt
import handler as hdl
import db_manager as dbm

if __name__ == "__main__":
    print("Bem vindo ao Cashd, seus dados serão salvos em:", dbm.WORK_DIR)
    print("\nAtalhos disponíveis:")
    for a, b in zip(*hdl.SHORTCUTS):
        print(a.ljust(6), b)

    ppt.prompt_entry()
