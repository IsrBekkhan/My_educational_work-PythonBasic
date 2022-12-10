class Stack(list):

    def __str__(self):
        return '; '.join(self)

    def add_element(self, element):
        self.append(element)

    def remove_element(self):
        if len(self) == 0:
            return None
        return self.pop()


class TaskManager(dict):

    def __str__(self):
        display = []
        if self:
            for i_priority in sorted(self.keys()):
                display.append('{} {} \n'.format(
                    i_priority, self[i_priority]
                ))
        return ''.join(display)

    def new_task(self, task, priority):
        if not self.is_exist(task):
            if priority not in self:
                self[priority] = Stack()
            self[priority].add_element(task)

    def is_exist(self, task):
        for task_list in self.values():
            if task in task_list:
                return True

    def remove_task(self, task):
        for task_list in self.values():
            if task in task_list:
                task_list.remove(task)
                break


# Код для теста
manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
manager.remove_task('поесть')
print(manager)
