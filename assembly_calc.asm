section .data
hey db 'Addy: ',0
h1 equ $-hey
wow db 0

yo db 'Mully: ',0
y1 equ $-yo
bam db 0

section .text
global _start

_start:

mov al,4
mov bl,2

add al,2
add al,'0'
mov [wow],al

mov al,4
mul bl
add al,'0'
mov [bam],al

mov eax,4
mov ebx,1
mov ecx,hey
mov edx,h1
int 0x80

mov eax,4
mov ebx,1
mov ecx,wow
mov edx,1
int 0x80

mov eax,4
mov ebx,1
mov ecx,yo
mov edx,y1
int 0x80

mov eax,4
mov ebx,1
mov ecx,bam
mov edx,1
int 0x80

mov eax,1
mov ebx,0
int 0x80
