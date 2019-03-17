from host.simple_call import sqrt
from host.value import PI
from interpret.term import interpret_term
from interpret.test import init_test_frame_stack
from machine import MachineExpressionStack
from machine import MachineNumber
from numpy import int32
from syntax import SyntaxBlock
from syntax import SyntaxComment
from syntax import SyntaxExpression
from syntax import SyntaxIdentifier
from syntax import SyntaxNumber
from syntax import SyntaxTerm


def init_term_block(term: SyntaxTerm) -> SyntaxBlock:
    return SyntaxBlock([SyntaxExpression([term])])


def test_interpret_number():
    term = SyntaxNumber(int32(100))
    frame_stack = init_test_frame_stack(
        init_term_block(term), MachineExpressionStack([])
    )
    interpret_term(frame_stack)
    assert frame_stack == init_test_frame_stack(
        init_term_block(term),
        MachineExpressionStack([MachineNumber(int32(100))]),
        term_index=1,
    )


def test_interpret_identifier_value():
    term = SyntaxIdentifier(PI.name)
    expression_stack = MachineExpressionStack([])
    frame_stack = init_test_frame_stack(
        init_term_block(term), expression_stack
    )
    interpret_term(frame_stack)
    assert frame_stack == init_test_frame_stack(
        init_term_block(term),
        MachineExpressionStack([PI.value]),
        term_index=1,
    )


def test_interpret_identifier_call():
    term = SyntaxIdentifier(sqrt.name)
    expression_stack = MachineExpressionStack(
        [MachineNumber(int32(16))]
    )
    frame_stack = init_test_frame_stack(
        init_term_block(term), expression_stack
    )
    interpret_term(frame_stack)
    assert frame_stack == init_test_frame_stack(
        init_term_block(term),
        MachineExpressionStack([MachineNumber(int32(4))]),
        term_index=1,
    )


def test_interpret_comment():
    term = SyntaxComment("something")
    expression_stack = MachineExpressionStack(
        [MachineNumber(int32(10))]
    )
    frame_stack = init_test_frame_stack(
        init_term_block(term), expression_stack
    )
    interpret_term(frame_stack)
    assert frame_stack == init_test_frame_stack(
        init_term_block(term),
        MachineExpressionStack([MachineNumber(int32(10))]),
        term_index=1,
    )
