struct ListNode* deleteDuplicates(struct ListNode* head){
    struct ListNode* current = head;
    while(current){
        while(current->next && current->next->val == current->val){
            current->next = current->next->next;
        }
        current = current->next;
    }
    return head;
}
