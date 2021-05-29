# finding permutations using recursion

portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]


def permutations(route, ports):
    # base case: when list of ports is empty output the route
    if not ports:
        print(' '.join([portnames[port] for port in route]))
    else:
        # we want to go through each port in the remaining ports list
        for i in range(len(ports)):
            # [a , [b, c...]] becomes [a, b, [c...]] , [a, c, [b...]]
            permutations(route+[ports[i]], ports[:i]+ports[i+1:])


# this will start the recursion with 0 as the first stop
permutations([0], list(range(1, len(portnames))))
