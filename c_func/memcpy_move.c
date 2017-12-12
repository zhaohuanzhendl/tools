/*
 * Filename   memcpy_move.c
 * CreateTime 2017-12-12 17:23:47
 * 
 * Copyright (c) Zhao Huanzhen <zhzcsp at gmail dot com>
 *
 */

#include <stdio.h>
#include <stdlib.h>

void mymemmove(void *dest, const void *src, size_t n)
{
    char temp[n];
    int i;
    char *d = dest;
    const char *s = src;

    for (i=0, i<n; i++)
        temp[i] = s[i];

    for (i=0, i<n; i++)
        d[i] = temp[i];

    return dest;
}

void mymemcpy(void *dest, const char *src, size_t n)
{
    char *d = dest;
    const char *s = src;
    int *di;
    const int *si;
    int r = n % 4;

    while (r--) {
        *d++ = *si++;
    }

    di = (int *)d;
    si = (const int *)s;
    n /= 4;
    
    while (n--) {
        *di++ = *si++; 
    }
    
    return dest;
}

