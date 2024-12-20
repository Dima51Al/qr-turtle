import qrcode
import turtle


def draw_qr_with_turtle(data):
    # Генерация QR-кода
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)


    qr_matrix = qr.get_matrix()


    turtle.tracer(0)
    turtle.penup()
    turtle.hideturtle()


    box_size = 10
    start_x = -len(qr_matrix) * box_size // 2
    start_y = len(qr_matrix) * box_size // 2


    for row in range(len(qr_matrix)):
        for col in range(len(qr_matrix[row])):
            if qr_matrix[row][col]:
                x = start_x + col * box_size
                y = start_y - row * box_size
                turtle.goto(x, y)
                turtle.dot(box_size, "black")

    turtle.done()


if __name__ == '__main__':
    link = input("Введите ссылку для генерации QR-кода: ")
    draw_qr_with_turtle(link)
