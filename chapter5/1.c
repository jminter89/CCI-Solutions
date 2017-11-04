/********************************************************
* You are given two 32-bit numbers, N and M, and two bit 
* positions, i and j Write a method to set all bits 
* between i and j in N equal to M (e g , M becomes a 
* substring of N located at i and starting at j)
* EXAMPLE:
* Input: N = 10000000000, M = 10101, i = 2, j = 6
* Output: N = 10001010100
*********************************************************/

#include <stdio.h>
#include <stdint.h>
#include <assert.h>

/********************************************************
 * setBits
 * @param (N) (32 bit integer)
 * @param (M) (32 bit integer)
 * @param (i) (right boundary of desired substring)
 * @param (j) (left boundary of desired substring)
 * @return (N with substring M in between indices i and j)
 * Time Complexity: O(n)
 * Time Complexity: O(n)
 *********************************************************/
int setBitsIJ(int32_t N, int32_t M, int32_t i, int32_t j)
{
	/* Create mask */
	uint32_t mask = 0xffff;
	mask = (mask << (31-j)) >> (31-j);
	mask = (mask >> i) << i;

	int32_t M_prime = M << i;
	return (N & ~mask) | (M_prime & mask);
}

int main( int argc, const char* argv[] )
{
	/* Example values */
	int32_t N = 0x400, M = 0x15, i = 2, j = 6, answ = 0x454;
	assert(setBitsIJ(N,M,i,j) == answ);
}
