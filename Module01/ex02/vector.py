# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 22:01:36 by dacortes          #+#    #+#              #
#    Updated: 2023/03/16 10:55:43 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vector:
    def __init__(self, values):
        self.values = values
        self.shape = (len(values), 1) if isinstance(values[0], list) else (1, len(values))
        
    def __str__(self):
        return str(self.values)
    
    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError("Vectors must be of the same shape")
        result = []
        for i in range(self.shape[0]):
            row = []
            for j in range(self.shape[1]):
                row.append(self.values[i][j] + other.values[i][j])
            result.append(row)
        return Vector(result)
    
    def __sub__(self, other):
        if self.shape != other.shape:
            raise ValueError("Vectors must be of the same shape")
        result = []
        for i in range(self.shape[0]):
            row = []
            for j in range(self.shape[1]):
                row.append(self.values[i][j] - other.values[i][j])
            result.append(row)
        return Vector(result)
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = []
            for i in range(self.shape[0]):
                row = []
                for j in range(self.shape[1]):
                    row.append(self.values[i][j] * other)
                result.append(row)
            return Vector(result)
        elif self.shape[1] != other.shape[0]:
            raise ValueError("Cannot multiply vectors of incompatible shapes")
        else:
            result = []
            for i in range(self.shape[0]):
                row = []
                for j in range(other.shape[1]):
                    val = sum([self.values[i][k] * other.values[k][j] for k in range(self.shape[1])])
                    row.append(val)
                result.append(row)
            return Vector(result)
    
    def __rmul__(self, other):
        return self * other
