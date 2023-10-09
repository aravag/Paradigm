sum([], 0).
sum([Head | Tail], Sum) :-
    sum(Tail, SumTail),
    Sum is Head + SumTail.
?- sum([1, 2, 3, 4, 5], X).