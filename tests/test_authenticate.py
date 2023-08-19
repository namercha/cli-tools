import pytest

from click.testing import CliRunner
from authenticate import auth

def test_non_admin_auth():
    # arrange 
    runner = CliRunner()
    prompt_inputs = '\n'.join([
        'nabs',
        'test',
        'test',
        'N'
    ])

    # act
    result = runner.invoke(auth, input=prompt_inputs)

    # asserts
    assert result.exit_code == 0
    
    expected_output = "\n".join([
        'username: nabs',
        'password: ',
        'Repeat for confirmation: ',
        'Are you an Admin? [y/N]: N',
        'Logging in nabs',
        ''
    ])
    assert result.output == expected_output


def test_admin_auth():
    # arrange 
    runner = CliRunner()
    prompt_inputs = '\n'.join([
        'nabs',
        'test',
        'test',
        'y',
        '354'
    ])

    # act
    result = runner.invoke(auth, input=prompt_inputs)

    # asserts
    assert result.exit_code == 0
    
    expected_output = "\n".join([
        'username: nabs',
        'password: ',
        'Repeat for confirmation: ',
        'Are you an Admin? [y/N]: y',
        'Admin ID> 354',
        'Logging in admin nabs ID = 354',
        ''
    ])
    assert result.output == expected_output
