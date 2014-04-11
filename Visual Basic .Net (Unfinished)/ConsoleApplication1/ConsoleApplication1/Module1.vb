Module Module1

    Sub Main()

        Dim row, col, t As Integer
        row = col = 10
        t = 1
        Dim endGame As Boolean = True
        Dim array2d(0 To 9, 0 To 9) As String
        array2d = init(array2d)
        display(array2d)

        While endGame
            array2d = turn(t, array2d)
            display(array2d)
            t = t * -1
            'endGame = False
        End While

        Console.ReadLine()

    End Sub

    Function turn(t, array2d)

        If t = 1 Then
            Return addToken("Player 1", "X", array2d)

        Else
            Return addToken("Player 2", "O", array2d)
        End If

        Return array2d

    End Function

    Function addToken(name, token, array2d)

        Dim added As Boolean = True
        Console.Write(name & " please choose a column" & vbCrLf)
        Dim col As String = Console.ReadLine()
        If col = "A" Then
            'Dim a(9) As String
            'a = array2d(0)
            Console.Write(array2d(0))

            'Console.Write(a(0))
            'array2d(0) = a
            display(array2d)
        End If
        Return array2d

    End Function

    Sub display(array2d)
        For i As Integer = 0 To 9
            For j As Integer = 0 To 9
                Console.Write(array2d(0, i) & " ")
            Next j
            Console.Write(vbCrLf)
        Next i
        Console.Write("===================" & vbCrLf & "A B C D E F G H I J" & vbCrLf & vbCrLf)
    End Sub

    Function init(array2d)
        For i As Integer = 0 To 9
            For j As Integer = 0 To 9
                array2d(i, j) = "-"
            Next j
        Next i
        'array2d(9, 0) = "X"
        Return array2d
    End Function

End Module
