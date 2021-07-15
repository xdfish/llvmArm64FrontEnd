
prog:	file format mach-o arm64


Disassembly of section __TEXT,__text:

0000000100003df8 <_add4>:
100003df8: ff 43 00 d1 	sub	sp, sp, #16
100003dfc: e0 0f 00 b9 	str	w0, [sp, #12]
100003e00: e8 0f 40 b9 	ldr	w8, [sp, #12]
100003e04: 08 11 00 11 	add	w8, w8, #4
100003e08: e8 0b 00 b9 	str	w8, [sp, #8]
100003e0c: e0 0b 40 b9 	ldr	w0, [sp, #8]
100003e10: ff 43 00 91 	add	sp, sp, #16
100003e14: c0 03 5f d6 	ret

0000000100003e18 <_add4_>:
100003e18: ff 43 00 d1 	sub	sp, sp, #16
100003e1c: e0 0f 00 b9 	str	w0, [sp, #12]
100003e20: e8 0f 40 b9 	ldr	w8, [sp, #12]
100003e24: 00 11 00 11 	add	w0, w8, #4
100003e28: ff 43 00 91 	add	sp, sp, #16
100003e2c: c0 03 5f d6 	ret

0000000100003e30 <_doMore>:
100003e30: ff 83 00 d1 	sub	sp, sp, #32
100003e34: e0 1f 00 b9 	str	w0, [sp, #28]
100003e38: e1 1b 00 b9 	str	w1, [sp, #24]
100003e3c: e2 17 00 b9 	str	w2, [sp, #20]
100003e40: e3 13 00 b9 	str	w3, [sp, #16]
100003e44: e8 1f 40 b9 	ldr	w8, [sp, #28]
100003e48: e9 1b 40 b9 	ldr	w9, [sp, #24]
100003e4c: 08 01 09 0b 	add	w8, w8, w9
100003e50: e8 0f 00 b9 	str	w8, [sp, #12]
100003e54: e8 17 40 b9 	ldr	w8, [sp, #20]
100003e58: e9 13 40 b9 	ldr	w9, [sp, #16]
100003e5c: 08 7d 09 1b 	mul	w8, w8, w9
100003e60: e8 0b 00 b9 	str	w8, [sp, #8]
100003e64: e8 0f 40 b9 	ldr	w8, [sp, #12]
100003e68: e9 0b 40 b9 	ldr	w9, [sp, #8]
100003e6c: 00 01 09 0b 	add	w0, w8, w9
100003e70: ff 83 00 91 	add	sp, sp, #32
100003e74: c0 03 5f d6 	ret

0000000100003e78 <_main>:
100003e78: ff c3 00 d1 	sub	sp, sp, #48
100003e7c: fd 7b 02 a9 	stp	x29, x30, [sp, #32]
100003e80: fd 83 00 91 	add	x29, sp, #32
100003e84: 08 00 80 52 	mov	w8, #0
100003e88: bf c3 1f b8 	stur	wzr, [x29, #-4]
100003e8c: a9 23 00 d1 	sub	x9, x29, #8
100003e90: bf 83 1f b8 	stur	wzr, [x29, #-8]
100003e94: 00 00 00 90 	adrp	x0, #0
100003e98: 00 00 3e 91 	add	x0, x0, #3968
100003e9c: e8 13 00 b9 	str	w8, [sp, #16]
100003ea0: e9 07 00 f9 	str	x9, [sp, #8]
100003ea4: 25 00 00 94 	bl	0x100003f38 <dyld_stub_binder+0x100003f38>
100003ea8: 09 00 00 90 	adrp	x9, #0
100003eac: 29 81 3e 91 	add	x9, x9, #4000
100003eb0: e0 03 09 aa 	mov	x0, x9
100003eb4: e9 03 00 91 	mov	x9, sp
100003eb8: ea 07 40 f9 	ldr	x10, [sp, #8]
100003ebc: 2a 01 00 f9 	str	x10, [x9]
100003ec0: 21 00 00 94 	bl	0x100003f44 <dyld_stub_binder+0x100003f44>
100003ec4: bf 43 1f b8 	stur	wzr, [x29, #-12]
100003ec8: a8 83 5f b8 	ldur	w8, [x29, #-8]
100003ecc: e0 03 08 aa 	mov	x0, x8
100003ed0: ca ff ff 97 	bl	0x100003df8 <_add4>
100003ed4: a0 43 1f b8 	stur	w0, [x29, #-12]
100003ed8: a0 43 5f b8 	ldur	w0, [x29, #-12]
100003edc: cf ff ff 97 	bl	0x100003e18 <_add4_>
100003ee0: a0 43 1f b8 	stur	w0, [x29, #-12]
100003ee4: a0 43 5f b8 	ldur	w0, [x29, #-12]
100003ee8: a8 83 5f b8 	ldur	w8, [x29, #-8]
100003eec: 01 11 00 11 	add	w1, w8, #4
100003ef0: a8 83 5f b8 	ldur	w8, [x29, #-8]
100003ef4: 02 09 00 71 	subs	w2, w8, #2
100003ef8: a8 83 5f b8 	ldur	w8, [x29, #-8]
100003efc: 03 31 00 11 	add	w3, w8, #12
100003f00: cc ff ff 97 	bl	0x100003e30 <_doMore>
100003f04: a0 43 1f b8 	stur	w0, [x29, #-12]
100003f08: a8 43 5f b8 	ldur	w8, [x29, #-12]
100003f0c: e4 03 08 aa 	mov	x4, x8
100003f10: 00 00 00 90 	adrp	x0, #0
100003f14: 00 8c 3e 91 	add	x0, x0, #4003
100003f18: e9 03 00 91 	mov	x9, sp
100003f1c: 24 01 00 f9 	str	x4, [x9]
100003f20: 06 00 00 94 	bl	0x100003f38 <dyld_stub_binder+0x100003f38>
100003f24: e8 13 40 b9 	ldr	w8, [sp, #16]
100003f28: e0 03 08 aa 	mov	x0, x8
100003f2c: fd 7b 42 a9 	ldp	x29, x30, [sp, #32]
100003f30: ff c3 00 91 	add	sp, sp, #48
100003f34: c0 03 5f d6 	ret

Disassembly of section __TEXT,__stubs:

0000000100003f38 <__stubs>:
100003f38: 1f 20 03 d5 	nop
100003f3c: 30 06 02 58 	ldr	x16, 0x100008000 <dyld_stub_binder+0x100008000>
100003f40: 00 02 1f d6 	br	x16
100003f44: 1f 20 03 d5 	nop
100003f48: 10 06 02 58 	ldr	x16, 0x100008008 <dyld_stub_binder+0x100008008>
100003f4c: 00 02 1f d6 	br	x16

Disassembly of section __TEXT,__stub_helper:

0000000100003f50 <__stub_helper>:
100003f50: 11 06 02 10 	adr	x17, #16576
100003f54: 1f 20 03 d5 	nop
100003f58: f0 47 bf a9 	stp	x16, x17, [sp, #-16]!
100003f5c: 1f 20 03 d5 	nop
100003f60: 10 05 00 58 	ldr	x16, 0x100004000 <dyld_stub_binder+0x100004000>
100003f64: 00 02 1f d6 	br	x16
100003f68: 50 00 00 18 	ldr	w16, 0x100003f70 <__stub_helper+0x20>
100003f6c: f9 ff ff 17 	b	0x100003f50 <__stub_helper>
100003f70: 00 00 00 00 	udf	#0
100003f74: 50 00 00 18 	ldr	w16, 0x100003f7c <__stub_helper+0x2c>
100003f78: f6 ff ff 17 	b	0x100003f50 <__stub_helper>
100003f7c: 0e 00 00 00 	udf	#14

Disassembly of section __TEXT,__cstring:

0000000100003f80 <__cstring>:
100003f80: 42 69 74 74 	<unknown>
100003f84: 65 20 67 65 	<unknown>
100003f88: 62 65 6e 20 	<unknown>
100003f8c: 53 69 65 20 	<unknown>
100003f90: 65 69 6e 65 	<unknown>
100003f94: 20 5a 61 68 	<unknown>
100003f98: 6c 20 65 69 	ldpsw	x12, x8, [x3, #-216]
100003f9c: 6e 3f 0a 00 	<unknown>
100003fa0: 25 64 00 25 	<unknown>
100003fa4: 64          	<unknown>
100003fa5: 0a          	<unknown>
100003fa6: 00          	<unknown>

Disassembly of section __TEXT,__unwind_info:

0000000100003fa8 <__unwind_info>:
100003fa8: 01 00 00 00 	udf	#1
100003fac: 1c 00 00 00 	udf	#28
100003fb0: 00 00 00 00 	udf	#0
100003fb4: 1c 00 00 00 	udf	#28
100003fb8: 00 00 00 00 	udf	#0
100003fbc: 1c 00 00 00 	udf	#28
100003fc0: 02 00 00 00 	udf	#2
100003fc4: f8 3d 00 00 	udf	#15864
100003fc8: 34 00 00 00 	udf	#52
100003fcc: 34 00 00 00 	udf	#52
100003fd0: 39 3f 00 00 	udf	#16185
100003fd4: 00 00 00 00 	udf	#0
100003fd8: 34 00 00 00 	udf	#52
100003fdc: 03 00 00 00 	udf	#3
100003fe0: 0c 00 03 00 	<unknown>
100003fe4: 18 00 03 00 	<unknown>
100003fe8: 00 00 00 02 	<unknown>
100003fec: 38 00 00 01 	<unknown>
100003ff0: 80 00 00 00 	udf	#128
100003ff4: 00 00 00 04 	<unknown>
100003ff8: 00 20 00 02 	<unknown>
100003ffc: 00 10 00 02 	<unknown>

Disassembly of section __DATA_CONST,__got:

0000000100004000 <__got>:
		...

Disassembly of section __DATA,__la_symbol_ptr:

0000000100008000 <__la_symbol_ptr>:
100008000: 68 3f 00 00 	udf	#16232
100008004: 01 00 00 00 	udf	#1
100008008: 74 3f 00 00 	udf	#16244
10000800c: 01 00 00 00 	udf	#1

Disassembly of section __DATA,__data:

0000000100008010 <__dyld_private>:
		...
