#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * main - zombies
 *
 * Description: make five zombies
 * Return: 0 for success
 */
int main(void)
{
	int i;
	pid_t myp_id;

	for (i = 0; i < 5; i++)
	{
		myp_id = fork();
		if (myp_id)
			printf("Zombie process created, PID: %i\n", myp_id);
		else
			exit(0);
	}
	return (0);
}
