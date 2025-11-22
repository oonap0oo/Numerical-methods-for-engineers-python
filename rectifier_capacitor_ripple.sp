* Simple RC circuit
V1 mains1 1 SIN(0 325 50)
Rs 1 mains2 1
D1 mains1 vp d1n4007
D2 0 mains1 d1n4007
D3 mains2 vp d1n4007
D4 0 mains2 d1n4007
C1 vp 0 220uF
R1 vp 0 5k

**********************************
* Model created by               *
*   Uni.Dipl.-Ing. Arpad Buermen *
*   arpad.burmen@ieee.org        *
* Copyright:                     *
*   Thomatronik GmbH, Germany    *
*   info@thomatronik.de          *
**********************************
* February 2001
*   SPICE3
.model d1n4007 d is = 1.09774E-008 n = 1.78309 rs = 0.0414388
+ eg = 1.11 xti = 3
+ cjo = 2.8173E-011 vj = 0.50772 m = 0.318974 fc = 0.5
+ tt = 9.85376E-006 bv = 1100 ibv = 0.1 af = 1 kf = 0

.tran .1ms 150ms UIC
.control
run
plot v(vp) v(mains1)-v(mains2)
.endc
.end

