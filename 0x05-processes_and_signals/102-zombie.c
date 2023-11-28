#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * main - crates 5 zombie processes
 *
 * Return: 0 (Always for success)
 */
int main(void)
{
	int i = 0;
	pid_t zabimaru;

	while (i < 5)
	{
		zabimaru = fork();

		if (!zabimaru)
			return (0);

		printf("Zombie process created, PID: %d\n", zabimaru);
		i++;
	}

	while (1)
		sleep(1);

	return (0);
}
