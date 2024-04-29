This is a DIY numpad that can be cut from many 2-3mm sheet goods, just make sure that your laser can handle it.  The one in the pictures is made from 3mm "Masonite" hardboard and painted with Rustoleum textured black. You will need screws.  I used #4-40 1/2" hex-head and ground down the excess length, but M3 should work as well.  The circles in the keyswitch cutouts will serve as spacers.  I used 8, but you will need all 12 if you cut from 2mm material, possibly 16 but I haven't checked; they're just 10mm circles with 3mm holes in the center. You will probably also want furniture bumpons or some other adhesive feet for grip.

The cut file includes holes suitable for mouting a Raspberry Pi Pico on headers.  One of the images is the wiring diagram for the specific RP2040 board I used.

Main.py is used with KMK keyboard firmware and would only work as expected if you use an RP2040 with an identical pinout.  It's probably better to think of it as a guide than a reusable asset.

Also, you need switches and keycaps. 22 must be 1u.  The extra two can be 1u to 1.75u.  There is no provision for stabilizers.

There are many other tools that can help generate files better matched to your specific needs, like Keyboard Layout Generator and Swill's plate generator. I used both.  I also used BeckerCAD 14 3D Pro to finalize the cut file and LaserGRBL to burn with a Comgrow Z1.
