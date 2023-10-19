.global _main
.align 2

_main:
    b _printf
    b _terminate

_printf:
    mov x0, #1
    adr x1, msg
    mov x2, len
    mov x16, #4
    svc 0

_terminate:
    mov x0, #0
    mov x16, #1
    svc 0

msg:
    .ascii "Hello, world!\n"

len = . - msg