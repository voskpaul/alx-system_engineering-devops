#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main(void)
{
    pid_t child_pid;
    int i;

    for (i = 0; i < 5; i++)
    {
        child_pid = fork();

        if (child_pid == -1)
        {
            perror("fork");
            exit(1);
        }

        if (child_pid == 0)
        {
            // This is the child process.
            exit(0);
        }
        else
        {
            // This is the parent process.
            printf("Zombie process created, PID: %d\n", child_pid);
        }
    }

    return (0);
}

