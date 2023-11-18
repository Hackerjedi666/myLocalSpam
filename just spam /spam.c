// Online C compiler to run C program online
#include <stdio.h>

int main() {
    int num_blocks, num_processes;
    printf("Enter the number of memory blocks: ");
    scanf("%d", &num_blocks);
    int blocks[num_blocks];
    for (int i = 0; i < num_blocks; i++) {
        printf("Enter the size of block %d: ", i);
        scanf("%d", &blocks[i]);
    }
    printf("Enter the number of processes: ");
    scanf("%d", &num_processes);
    int processes[num_processes];
    int allocated[num_processes];
    for (int i = 0; i < num_processes; i++) {
        printf("Enter the size of process %d: ", i);
        scanf("%d", &processes[i]);
        allocated[i] = 0;
    }
    for (int i = 0; i < num_processes; i++) {
        for (int j = 0; j < num_blocks; j++) {
            if (blocks[j] >= processes[i] && !allocated[i]) {
                printf("The process %d allocated to %d\n", i, blocks[j]);
                allocated[i] = 1;
                blocks[j] -= processes[i];
            }
        }
        if (!allocated[i]) {
            printf("The process %d could not be allocated\n", i);
        }
    }
    return 0;
}