# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')

    inp12=2
    sel =12
    dut.sel.value = sel
    dut.inp12.value = inp12

    await Timer(2, units='ns')
    
    assert dut.out.value == inp12, "MUX is not working properly: {inp12} != {out}, expected value={EXP}".format(
            inp5=int(dut.inp12.value), sel=int(dut.sel.value), out=int(dut.out.value), EXP=inp12)
            

