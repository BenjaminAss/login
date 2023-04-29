from PIL import ImageTk, Image

def leer_imagen (path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ANTIALIAS))


def centrar_root(root, aplic_ancho, aplic_largo):
    pantalla_ancho = root.winfo_screenwidth()
    pantalla_largo = root.winfo_screenheight()
    x = int((pantalla_ancho/2) - (aplic_ancho/2))
    y = int((pantalla_largo/2) - (aplic_largo/2))
    return root.geometry(f"{aplic_ancho}x{aplic_largo}+{x}+{y}")