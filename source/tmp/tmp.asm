
CONVERT/prog:	file format mach-o arm64


Disassembly of section __TEXT,__text:

0000000100003df8 <_add4>:
100003df8:     	sub	sp, sp, #16
100003dfc:     	str	w0, [sp, #12]
100003e00:     	ldr	w8, [sp, #12]
100003e04:     	add	w8, w8, #4
100003e08:     	str	w8, [sp, #8]
100003e0c:     	ldr	w0, [sp, #8]
100003e10:     	add	sp, sp, #16
100003e14:     	ret

0000000100003e18 <_add4_>:
100003e18:     	sub	sp, sp, #16
100003e1c:     	str	w0, [sp, #12]
100003e20:     	ldr	w8, [sp, #12]
100003e24:     	add	w0, w8, #4
100003e28:     	add	sp, sp, #16
100003e2c:     	ret

0000000100003e30 <_doMore>:
100003e30:     	sub	sp, sp, #32
100003e34:     	str	w0, [sp, #28]
100003e38:     	str	w1, [sp, #24]
100003e3c:     	str	w2, [sp, #20]
100003e40:     	str	w3, [sp, #16]
100003e44:     	ldr	w8, [sp, #28]
100003e48:     	ldr	w9, [sp, #24]
100003e4c:     	add	w8, w8, w9
100003e50:     	str	w8, [sp, #12]
100003e54:     	ldr	w8, [sp, #20]
100003e58:     	ldr	w9, [sp, #16]
100003e5c:     	mul	w8, w8, w9
100003e60:     	str	w8, [sp, #8]
100003e64:     	ldr	w8, [sp, #12]
100003e68:     	ldr	w9, [sp, #8]
100003e6c:     	add	w0, w8, w9
100003e70:     	add	sp, sp, #32
100003e74:     	ret

0000000100003e78 <_main>:
100003e78:     	sub	sp, sp, #48
100003e7c:     	stp	x29, x30, [sp, #32]
100003e80:     	add	x29, sp, #32
100003e84:     	mov	w8, #0
100003e88:     	stur	wzr, [x29, #-4]
100003e8c:     	sub	x9, x29, #8
100003e90:     	stur	wzr, [x29, #-8]
100003e94:     	adrp	x0, #0
100003e98:     	add	x0, x0, #3968
100003e9c:     	str	w8, [sp, #16]
100003ea0:     	str	x9, [sp, #8]
100003ea4:     	bl	0x100003f38 <dyld_stub_binder+0x100003f38>
100003ea8:     	adrp	x9, #0
100003eac:     	add	x9, x9, #4000
100003eb0:     	mov	x0, x9
100003eb4:     	mov	x9, sp
100003eb8:     	ldr	x10, [sp, #8]
100003ebc:     	str	x10, [x9]
100003ec0:     	bl	0x100003f44 <dyld_stub_binder+0x100003f44>
100003ec4:     	stur	wzr, [x29, #-12]
100003ec8:     	ldur	w8, [x29, #-8]
100003ecc:     	mov	x0, x8
100003ed0:     	bl	0x100003df8 <_add4>
100003ed4:     	stur	w0, [x29, #-12]
100003ed8:     	ldur	w0, [x29, #-12]
100003edc:     	bl	0x100003e18 <_add4_>
100003ee0:     	stur	w0, [x29, #-12]
100003ee4:     	ldur	w0, [x29, #-12]
100003ee8:     	ldur	w8, [x29, #-8]
100003eec:     	add	w1, w8, #4
100003ef0:     	ldur	w8, [x29, #-8]
100003ef4:     	subs	w2, w8, #2
100003ef8:     	ldur	w8, [x29, #-8]
100003efc:     	add	w3, w8, #12
100003f00:     	bl	0x100003e30 <_doMore>
100003f04:     	stur	w0, [x29, #-12]
100003f08:     	ldur	w8, [x29, #-12]
100003f0c:     	mov	x4, x8
100003f10:     	adrp	x0, #0
100003f14:     	add	x0, x0, #4003
100003f18:     	mov	x9, sp
100003f1c:     	str	x4, [x9]
100003f20:     	bl	0x100003f38 <dyld_stub_binder+0x100003f38>
100003f24:     	ldr	w8, [sp, #16]
100003f28:     	mov	x0, x8
100003f2c:     	ldp	x29, x30, [sp, #32]
100003f30:     	add	sp, sp, #48
100003f34:     	ret

Disassembly of section __TEXT,__stubs:

0000000100003f38 <__stubs>:
100003f38:     	nop
100003f3c:     	ldr	x16, 0x100008000 <dyld_stub_binder+0x100008000>
100003f40:     	br	x16
100003f44:     	nop
100003f48:     	ldr	x16, 0x100008008 <dyld_stub_binder+0x100008008>
100003f4c:     	br	x16

Disassembly of section __TEXT,__stub_helper:

0000000100003f50 <__stub_helper>:
100003f50:     	adr	x17, #16576
100003f54:     	nop
100003f58:     	stp	x16, x17, [sp, #-16]!
100003f5c:     	nop
100003f60:     	ldr	x16, 0x100004000 <dyld_stub_binder+0x100004000>
100003f64:     	br	x16
100003f68:     	ldr	w16, 0x100003f70 <__stub_helper+0x20>
100003f6c:     	b	0x100003f50 <__stub_helper>
100003f70:     	udf	#0
100003f74:     	ldr	w16, 0x100003f7c <__stub_helper+0x2c>
100003f78:     	b	0x100003f50 <__stub_helper>
100003f7c:     	udf	#14

Disassembly of section __TEXT,__cstring:

0000000100003f80 <__cstring>:
100003f80:     	<unknown>
100003f84:     	<unknown>
100003f88:     	<unknown>
100003f8c:     	<unknown>
100003f90:     	<unknown>
100003f94:     	<unknown>
100003f98:     	ldpsw	x12, x8, [x3, #-216]
100003f9c:     	<unknown>
100003fa0:     	<unknown>
100003fa4:     	<unknown>
100003fa5:     	<unknown>
100003fa6:     	<unknown>

Disassembly of section __TEXT,__unwind_info:

0000000100003fa8 <__unwind_info>:
100003fa8:     	udf	#1
100003fac:     	udf	#28
100003fb0:     	udf	#0
100003fb4:     	udf	#28
100003fb8:     	udf	#0
100003fbc:     	udf	#28
100003fc0:     	udf	#2
100003fc4:     	udf	#15864
100003fc8:     	udf	#52
100003fcc:     	udf	#52
100003fd0:     	udf	#16185
100003fd4:     	udf	#0
100003fd8:     	udf	#52
100003fdc:     	udf	#3
100003fe0:     	<unknown>
100003fe4:     	<unknown>
100003fe8:     	<unknown>
100003fec:     	<unknown>
100003ff0:     	udf	#128
100003ff4:     	<unknown>
100003ff8:     	<unknown>
100003ffc:     	<unknown>

Disassembly of section __DATA_CONST,__got:

0000000100004000 <__got>:
		...

Disassembly of section __DATA,__la_symbol_ptr:

0000000100008000 <__la_symbol_ptr>:
100008000:     	udf	#16232
100008004:     	udf	#1
100008008:     	udf	#16244
10000800c:     	udf	#1

Disassembly of section __DATA,__data:

0000000100008010 <__dyld_private>:
		...
