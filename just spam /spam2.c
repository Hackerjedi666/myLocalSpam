#include <stdio.h>

void implimentWorstFit(int blockSize[], int blocks, int processSize[], int processes){
    // This will store the block id of the allocated block to a process
    int allocation[processes];
    int occupied[blocks];
    int ogSize[blocks];
    // initially assigning -1 to all allocation indexes
    // means nothing is allocated currently
    for(int i = 0; i < processes; i++){
        allocation[i] = -1;
    }
    
    for(int i = 0; i < blocks; i++){
        occupied[i] = 0;
        ogSize[i] = blockSize[i];
    }

    for (int i=0; i < processes; i++){
	int indexPlaced = -1;
	for(int j = 0; j < blocks; j++)
	{
	    // if not occupied and block size is large enough
	    if(blockSize[j] >= processSize[i] && !occupied[j])
            {
                // place it at the first block fit to accomodate process
                if (indexPlaced == -1)
                    indexPlaced = j;
                    
                // if any future block is larger than the current block where
                // process is placed, change the block and thus indexPlaced
                else if (blockSize[indexPlaced] < blockSize[j])
                    indexPlaced = j;
            }
        }
 
        // If we were successfully able to find block for the process
        if (indexPlaced != -1)
        {
            // allocate this block j to process p[i]
            allocation[i] = indexPlaced;
            
            // make the status of the block as occupied
            occupied[indexPlaced] = 1;
            blockSize[indexPlaced] -= processSize[i];
        }
    }
 
    printf("\nFile No.\tFile Size\tBlock no.\tBlock Size \tFragment Size\n");
    for (int i = 0; i < processes; i++)
    {
        printf("%d \t\t\t %d \t\t\t", i+1, processSize[i]);
        if (allocation[i] != -1)
            printf("%d \t\t\t %d \t\t\t %d \n",i + 1, ogSize[i], blockSize[i]);
        else
            printf("Not Allocated\n");
    }
}
 
// Driver code
int main()
{
    int num_blocks, num_processes;
    printf("Enter the number of memory blocks: ");
    scanf("%d", &num_blocks);
    int blocks[num_blocks];
    printf("Enter the number of files: ");
    scanf("%d", &num_processes);
    int processes[num_processes];
    for (int i = 0; i < num_blocks; i++) {
        printf("Enter the size of block %d: ", i+1);
        scanf("%d", &blocks[i]);
    }
    for (int i = 0; i < num_processes; i++) {
        printf("Enter the size of file %d: ", i+1);
        scanf("%d", &processes[i]);
    }
    implimentWorstFit(blocks, num_blocks, processes, num_processes);
 
    return 0;
}