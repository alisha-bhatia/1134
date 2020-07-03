def merge_linked_lists(srt_list1, srt_list2):
     def merge_sublists(n1, n2, res):
          if n1.data is None and n2.data is None:
               return
          if n2.data is None or (n1.data and n1.data < n2.data):
               result.add_last(n1.data)
               merge_sublists(n1.next, n2, res)
               return
          if n1.data is None or (n2.data and n1.data >= n2.data):
               result.add_last(n2.data)
               merge_sublists(n1, n2.next, res)
               return
          result = DoublyLinkedList()
          merge_sublists(srt_list1.first_node(), srt_list2.first_node(), result)
          return result
