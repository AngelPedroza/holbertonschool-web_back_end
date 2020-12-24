export default function getListStudentIds(list) {
    if (Array.isArray(list)) {
        return [];
    }

    const ids = list.map((el) => el.id);

    return ids;
}