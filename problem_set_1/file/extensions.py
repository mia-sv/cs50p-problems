name = input("File name: ").lower().strip()
name_parts = name.split(".") 

match name_parts[-1]:
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "gif":
        print("image/gif")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")




