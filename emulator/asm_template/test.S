#*****************************************************************************
# test.S
#-----------------------------------------------------------------------------
#
# Test bounds checking instruction.
#

.section .text

.global bon
.type void, @function
bon:
    li t0, 0x1
    sll t0, t0, 63
    add t0, t0, a0
    csrw 0x800, t0
    ret

.global boff
.type void, @function
boff:
    csrw 0x800, zero

.global kenny1
.type void, @function
kenny1:
	addi t0, a0, 0
	addi t1, a0, 4
	bndr a0, t0, t1
	sbdl a0, 0(a1)
	sbdu a0, 0(a1)
	bndr a0, x0, x0
	lbdls a0, 0(a1)
	lbdus a0, 0(a1)
	lw.b a1, 0(a0)
    ret		
	
.global store8
.type void, @function
store8:
    sd.b a1, 0(a0)
    ret

.global store4
.type void, @function
store4:
    sw.b a1, 0(a0)
    ret

.global store2
.type void, @function
store2:
    sh.b a1, 0(a0)
    ret

.global store1
.type void, @function
store1:
    sb.b a1, 0(a0)
    ret

.global load8
.type uint64_t, @function
load8:
    ld.b a1, 0(a0)
    ret

.global load4
.type uint32_t, @function
load4:
    lw.b a1, 0(a0)
    ret

.global load2
.type uint16_t, @function
load2:
    lh.b a1, 0(a0)
    ret

.global load1
.type uint8_t, @function
load1:
    lb.b a1, 0(a0)
    ret

.global set_bound
.type void_ptr, @function
set_bound:
    bndr a0, a1, a2
    ret
