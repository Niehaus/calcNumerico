#!/usr/bin/env
#-*- coding: utf-8 -*-

import pivotamento

def Superior(A, b):
  Ln = len(b)
  cn = Ln
  for Li in range(0, Ln-1, 1):
    A[:], b[:] = pivotamento.pivo(Li, b, A)
    for Lj in range(Li+1, Ln, 1):
      lam   =  A[Lj][Li] /A[Li][Li]
      b[Lj] = b[Lj] - b[Li] * lam
      for ci in range(Li, cn, 1):
        A[Lj][ci] =  A[Lj][ci] - A[Li][ci] * lam
  return (b, A)
