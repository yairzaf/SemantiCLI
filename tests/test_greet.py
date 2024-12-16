def test_greet(parser, capsys):
    args = parser.parse_args(['greet', 'Test'])
    from semanticli.commands.greet import run
    run(args)
    captured = capsys.readouterr()
    assert "Hello, Test!" in captured.out