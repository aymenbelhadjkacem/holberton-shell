#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * main - creates five zombie process.
 * Return: Always 0.
 */

int infinite_while(void);

int main(void)

{
	int child_pid1, child_pid2, child_pid3, child_pid4, child_pid5;

	child_pid1 = fork();
	if (child_pid1 == 0)
	{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}
	child_pid2 = fork();
	if (child_pid2 == 0)
	{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}
	child_pid3 = fork();
	if (child_pid3 == 0)
	{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}
	child_pid4 = fork();
	if (child_pid4 == 0)
	{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}
	child_pid5 = fork();
	if (child_pid5 == 0)
	{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}
	infinite_while();
	return (0);
}

/**
 *infinite_while - creates an infinite loop
 *Return: Always 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
