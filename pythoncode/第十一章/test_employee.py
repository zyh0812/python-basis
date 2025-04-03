from employee import Employee

def test_give_default_raise():
    message = Employee('zhou','yuhong','5000')

    assert message.give_raise == '10000'

